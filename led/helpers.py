from MQTTHandler import *


def init():
    """initialize MQTT Connection
    """
    pass


def rgb(client, r: int, g: int, b: int):
    """set rgb value for a given client

    Parameters
    ----------
    client : [type]
        the controller to set the color for
    r : int
        r value of the color
    g : int
        g value of the color
    b : int
        b value of the color
    """
    pass


def getDevices() -> list:
    """get connected device

    Returns
    -------
    list
        list of connected devices
    """
    pass


def disconnect(client):
    """disconnect a given client

    Parameters
    ----------
    client : [type]
        the client to disconnect
    """
    pass
