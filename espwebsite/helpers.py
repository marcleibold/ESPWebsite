from espwebsite.NetworkHandler import NetworkHandler
from espwebsite import config


networkHandler = NetworkHandler()


def getControllersHTML(activeControllers):
    controllersHTML = ""
    controllerHTMLTemplate = open(
        "espwebsite/templates/controlsWrapper.html").read()

    if len(activeControllers) > 0:
        for esp in activeControllers:
            colorsHTML = ""

            for i, color in enumerate(esp['customColors']):
                colorsHTML += """<button id="%s_custom%d" class="customColor" style="background-color: %s;"></button>""" % (
                    esp['name'], i, color)

            controllerHTML = controllerHTMLTemplate.replace(
                "phName", esp['name'])
            controllerHTML = controllerHTML.replace(
                "phColors", colorsHTML)

            controllersHTML += controllerHTML
    else:
        return ""

    return controllersHTML


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
            deviceData[mac]["name"] = mac
            device["name"] = device["mac"]
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
        deviceData[mac]["name"] = name
        addController(deviceData[mac])
        config.set("deviceData", deviceData)
        return 1
    return 0


def disconnect(data):
    deviceData = config.get("deviceData")
    data["ip"] = deviceData[data["mac"]]["ip"]
    isDisconnected = networkHandler.disconnectClient(data)
    if isDisconnected:
        removeController(data)
        return 1
    return 0


def addController(data):
    deviceData = config.get("deviceData")
    if data["mac"] in deviceData:
        if "customColors" in deviceData[data["mac"]]:
            customColors = deviceData[data["mac"]]["customColors"]
        else:
            customColors = []
    else:
        customColors = []

    controller = {
        "name": data["name"],
        "customColors": customColors
    }

    print(controller)

    config.addController(controller)


def removeController(data):
    name = config.get("deviceData")[data["mac"]]["name"]
    config.removeController(name)


def updateConnected():
    connectedDevices = getConnectedDevices()
    print("update")
    config.set("connectedDevices", connectedDevices)
