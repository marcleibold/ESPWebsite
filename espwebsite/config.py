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
