from espwebsite.NetworkHandler import NetworkHandler
from espwebsite import config


networkHandler = NetworkHandler()


# def getControllersHTML(activeControllers):
#     controllersHTML = ""
#     controllerHTMLTemplate = open(
#         "espwebsite/templates/controlsWrapper.html").read()

#     if len(activeControllers) > 0:
#         for esp in activeControllers:
#             colorsHTML = ""

#             for i, color in enumerate(esp['customColors']):
#                 colorsHTML += """<button id="%s_custom%d" class="customColor" style="background-color: %s;"></button>""" % (
#                     esp['name'], i, color)

#             controllerHTML = controllerHTMLTemplate.replace(
#                 "phName", esp['name'])
#             controllerHTML = controllerHTML.replace(
#                 "phColors", colorsHTML)

#             controllersHTML += controllerHTML
#     else:
#         return ""

#     return controllersHTML


def getWaitingDevices():
    networks = networkHandler.getMicrocontrollerNetworks()
    waitingDevices = []
    for network in networks:
        waitingDevices += [{
            "mac": network.split("_")[0]
        }]
    return waitingDevices


def getConnectedDevices():
    connectedDevices = networkHandler.getConnected()
    deviceData = config.get("deviceData")
    for device in connectedDevices:
        mac = device["mac"]
        if device["mac"] in deviceData:
            device["name"] = deviceData[mac]["name"]
            for key in device:
                deviceData[mac][key] = device[key]
        else:
            deviceData[mac] = device
            deviceData[mac]["name"] = "_".join(mac.split(":"))
            deviceData[mac]["customColors"] = []
            device["name"] = "_".join(device["mac"].split(":"))
    config.set("deviceData", deviceData)
    return connectedDevices


def connect(data):
    mac = data["mac"]
    name = data["name"]
    deviceData = config.get("deviceData")
    isConnected = networkHandler.connectClient(data)
    if isConnected:
        if mac not in deviceData:
            deviceData[mac] = {"mac": mac}
            deviceData[mac]["customColors"] = []
        deviceData[mac]["name"] = name
        config.set("deviceData", deviceData)
        config.add("connectedDevices", deviceData[mac])
        return 1
    return 0


def disconnect(data):
    deviceData = config.get("deviceData")
    data["ip"] = deviceData[data["mac"]]["ip"]
    isDisconnected = networkHandler.disconnectClient(data)
    if isDisconnected:
        config.removeDevice(data)
        return 1
    return 0


def updateConnected():
    connectedDevices = getConnectedDevices()
    config.set("connectedDevices", connectedDevices)
