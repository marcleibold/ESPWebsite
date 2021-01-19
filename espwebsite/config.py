config = {
    "activeControllers": [
        {
            "name": "TestESP",
            "customColors": [
                "red",
                "green",
                "blue"
            ]
        },
        {
            "name": "TestESP2",
            "customColors": [
                "blue",
                "green",
                "blue"
            ]
        }
    ],
    "deviceData": {}
}


def get(configEntry):
    if configEntry in config:
        return config[configEntry]
    else:
        return False


def set(configEntry, value):
    if configEntry in config:
        config[configEntry] = value
        return True
    else:
        return False


def addController(controller):
    config["activeControllers"].append(controller)


def removeController(name):
    for i, controller in enumerate(config["activeControllers"]):
        if controller["name"] == name:
            config["activeControllers"].pop(i)
