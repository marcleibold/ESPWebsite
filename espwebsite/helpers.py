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
