from espwebsite.NetworkHandler import NetworkHandler
from espwebsite import config
import subprocess


networkHandler = NetworkHandler()


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


def setRGB(data):
    """send Color as rgb to microcontroller

    #### Args:
        data (dict): dict with name and rgb values

    #### Returns:
        status (boolean): boolean value if API call succeeded
    """
    deviceData = config.get("deviceData")
    for device in deviceData:
        if deviceData[device]["name"] == data["name"]:
            cmd = 'curl -XPOST http://{}:8080/rgb -d "{}" -v -m 5'.format(
                deviceData[device]["ip"], str(data["rgbb"]))
            print(cmd)
            try:
                output = subprocess.check_output(cmd, shell=True)
            except subprocess.CalledProcessError as e:
                return False
            else:

                return True
