# HTD Lync12 Series integration for Home Assistant

This integration will add the HTD Lync12 into Home Assistant.

## Installation steps

1. Download the 4 files (`__init__.py`, `htd_lync12.py`, `media_player.py`, `manifest.json`) from this repo and place them into your `custom_components/htd_lync12` folder.
2. Update your configuration.yaml to include the following (NOTE: Only host is required).

htd_lync12:
  - host: 192.168.1.133
    zones:
      - Master Bedroom
      - Master Bathroom
      - Bedroom 1
      - Kitchen
      - Living Room
      - Fireplace Porch
      - Deck at Living Room
      - Deck at Master Bedroom
      - Upstairs Den
      - Bedroom 2
      - Bedroom 3
      - Bonus Room

    sources:
      - NA 1
      - NA 2
      - NA 3
      - Bluetooth
      - NA 5
      - NA 6
      - NA 7
      - NA 8
      - NA 9
      - NA 10
      - NA 11
      - NA 12
      - NA 13
      - NA 14
      - NA 15
      - Airplay
      - Alexa
      - MP3 Player

3. Restart Home Assistant


## ChangeLog
- March 9, 2021 - Intial Release


## Code Credits
- https://github.com/hikirsch/htd_mc-home-assistant
- https://github.com/whitingj/mca66
- https://github.com/steve28/mca66
- http://www.brandonclaps.com/?p=173
