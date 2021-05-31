from espwebsite.NetworkHandler import NetworkHandler
from espwebsite import config
import subprocess
import time


networkHandler = NetworkHandler()
lastCall = 0


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
            device["color"] = deviceData[mac]["color"]
            device["onState"] = deviceData[mac]["onState"]
            for key in device:
                deviceData[mac][key] = device[key]
        else:
            deviceData[mac] = device
            deviceData[mac]["name"] = "_".join(mac.split(":"))
            deviceData[mac]["customColors"] = []
            deviceData[mac]["color"] = {
                "r": 255, "g": 255, "b": 255, "brightness": 150}
            deviceData[mac]["onState"] = 0
            device["name"] = "_".join(device["mac"].split(":"))
    config.set("deviceData", deviceData)
    config.set("connectedDevices", connectedDevices)
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
            deviceData[mac]["color"] = {
                "r": 255, "g": 255, "b": 255, "brightness": 150}
            deviceData[mac]["onState"] = 0
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
    global lastCall
    if time.time() - lastCall >= 0.1:
        deviceData = config.get("deviceData")
        for device in deviceData:
            if deviceData[device]["name"] == data["name"]:
                cmd = 'curl -XPOST http://{}:8080/rgb -d "{}" -v -m 0.5'.format(
                    deviceData[device]["ip"], str(data["rgbb"]))
                print(cmd)
                try:
                    output = subprocess.check_output(cmd, shell=True)
                except subprocess.CalledProcessError as e:
                    return False
                else:
                    lastCall = time.time()

                    if data["rgbb"] == {"r": 0, "g": 0, "b": 0, "brightness": 0}:
                        deviceData[device]["onState"] = 0
                    else:
                        deviceData[device]["color"] = data["rgbb"]
                        deviceData[device]["onState"] = 1
                    config.set("deviceData", deviceData)

                    connectedDevices = config.get("connectedDevices")
                    for device in connectedDevices:
                        if device["name"] == data["name"]:
                            if data["rgbb"] == {"r": 0, "g": 0, "b": 0, "brightness": 0}:
                                device["onState"] = 0
                            else:
                                device["onState"] = 1
                    config.set("connectedDevices", connectedDevices)
                    return True
