# ESPWebsite
A simple flask website to manage and monitor ESP8266 microchips from a Raspberry Pi.\
The ESPs will be used to control LED strips.

Basic functionality is already working

#### Corresponding Repository:
[ESP API](https://github.com/marcleibold/ESPLED)

## Prerequisites
- Machine needs to be connected to a Network via Ethernet
- Machine needs to have a Wifi Interface
- .env File containing WIFI_SSID and WIFI_PASS of main Network

## How to run
cd into the Directory and execute the following command:
```bash
FLASK_APP=run.py python3 -m flask run --no-debugger --host=192.168.178.XX > /dev/null & 
```
(replace the IP address with the address of you machine)

## Built with
- [Flask](https://flask.palletsprojects.com/)
- [iro.js](https://iro.js.org/)
