"""Support for Home Theatre Direct's Lync12 series"""
import voluptuous as vol

from homeassistant.core import HomeAssistant
from homeassistant.helpers import config_validation as cv, discovery
from homeassistant.const import CONF_HOST, CONF_PORT, CONF_PASSWORD, CONF_USERNAME
import homeassistant.helpers.config_validation as cv
from homeassistant.helpers.typing import ConfigType

from .htd_lync12 import DEFAULT_HTD_LYNC12_PORT, HtdLync12Client

DOMAIN = "htd_lync12"

CONF_ZONES = "zones"
CONF_SOURCES = "sources"

CONFIG_SCHEMA = vol.Schema(
    {
        DOMAIN: vol.Schema(
            [{
                vol.Required(CONF_HOST): cv.string,
                vol.Optional(CONF_PORT, default=DEFAULT_HTD_LYNC12_PORT): cv.port,
                vol.Optional(CONF_ZONES): vol.All(
                    cv.ensure_list, [cv.string]
                ),
                vol.Optional(CONF_SOURCES): vol.All(
                    cv.ensure_list, [cv.string]
                ),
            }]
        )
    },
    extra=vol.ALLOW_EXTRA,
)

def setup(hass: HomeAssistant, config: ConfigType):
    htd_config = config.get(DOMAIN)

    configs = []

    for i in range(len(htd_config)):
        htd_item_config = htd_config[i]
        host = htd_item_config.get(CONF_HOST)
        port = htd_item_config.get(CONF_PORT)
        zones = htd_item_config.get(CONF_ZONES)
        sources = htd_item_config.get(CONF_SOURCES)

        if zones is None:
            zones = []
        
        if sources is None:
            sources = []

        # the device has 12 zones, so we default to Zone X
        for i in range(len(zones), 12):
            zones.append("Zone " + str(i + 1))

        # the device has 18 sources, so we default to Source X
        for i in range(len(sources), 18):
            sources.append("Source " + str(i + 1))
        
        configs.append({ 
            "zones": zones, 
            "sources": sources,
            "client": HtdLync12Client(host, port),
        })

    hass.data[DOMAIN] = configs

    for component in ("media_player",):
        discovery.load_platform(hass, component, DOMAIN, {}, config)

    return True
