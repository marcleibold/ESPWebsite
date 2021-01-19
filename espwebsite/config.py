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
    "deviceData": {},
    "connectedDevices": []
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


def add(configEntry, value):
    if configEntry in config:
        if type(config[configEntry]) == list:
            config[configEntry].append(value)


def addController(controller):
    config["activeControllers"].append(controller)


def removeController(name):
    for i, controller in enumerate(config["activeControllers"]):
        if controller["name"] == name:
            config["activeControllers"].pop(i)


def removeDevice(data):
    for i, device in enumerate(config["connectedDevices"]):
        if device["mac"] == data["mac"]:
            config["connectedDevices"].pop(i)
