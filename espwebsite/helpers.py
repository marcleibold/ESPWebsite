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
    devices = [
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
    return devices


def connect(mac):
    # TODO: implement proper connection workflow
    return 1
