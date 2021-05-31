import json

config = {}


def get(configEntry):
    if configEntry in config:
        save()
        return config[configEntry]

    else:
        return []


def set(configEntry, value):
    if configEntry in config:
        config[configEntry] = value
        save()
        return True
    else:
        return False


def add(configEntry, value):
    if configEntry in config:
        if type(config[configEntry]) == list:
            config[configEntry].append(value)
            save()


def addController(controller):
    config["activeControllers"].append(controller)
    save()


def removeController(name):
    for i, controller in enumerate(config["activeControllers"]):
        if controller["name"] == name:
            config["activeControllers"].pop(i)
            save()


def removeDevice(data):
    for i, device in enumerate(config["connectedDevices"]):
        if device["mac"] == data["mac"]:
            config["connectedDevices"].pop(i)
            save()


def getDefault():
    default = {
        "activeControllers": [],
        "deviceData": {},
        "connectedDevices": []
    }
    return default


def load():
    global config
    with open("config.json", "r") as f:
        config = json.load(f)


def save():
    with open("config.json", "w") as f:
        json.dump(config, f)
