waitingDevices = [
    {
        'mac': '00:1A:3F:F1:4C:C6'
    },
    {
        'mac': '02:9B:B0:CB:AA:FC'
    },
    {
        'mac': '10:F0:05:40:F3:22'
    }
]

connectedDevices = []


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
    # TODO: implement ESP Network querying
    return waitingDevices


def getConnectedDevices():
    return connectedDevices


def connect(data):
    # TODO: implement proper connection workflow
    global connectedDevices

    for device in waitingDevices:
        if device["mac"] == data["mac"]:
            waitingDevices.remove(device)
            connectedDevices += [device]
            return 1
    return 0


def disconnect(data):
    # TODO: implement proper disconnecting workflow
    for device in connectedDevices:
        if device["mac"] == data["mac"]:
            connectedDevices.remove(device)
            return 1
    return 0
