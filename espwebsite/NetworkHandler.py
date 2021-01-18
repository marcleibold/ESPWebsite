import netifaces
import subprocess
import re
import os
import time


class NetworkHandler:

    wifiInterface = ""
    ethInterface = ""

    def __init__(self):
        interfaces = netifaces.interfaces()
        self.wifiInterface = [
            interface for interface in interfaces if interface.startswith("wl") and not interface.startswith("wlx")
        ][0]
        self.ethInterface = [
            interface for interface in interfaces if interface.startswith("e")
        ][0]

    def search(self):
        """Get open Wifi networks nearby

        #### Returns:
            wifiNetworks (list): list of wifi network names
        """
        try:
            output = subprocess.check_output(
                "iwlist {} scan | grep -E 'Address|ESSID'".format(self.wifiInterface), shell=True).decode("utf-8")
        except:
            return set()
        networks_raw = re.split("Cell\ [0-9]{2}\ -\ ", output)
        networks = set()
        for network in networks_raw:
            parts = re.split("\s{2,}", network)
            if len(parts) > 1:
                if len(parts[0]) > 0:
                    ssid = parts[1].split("ID:")[1].strip().strip('"')
                    mac = parts[0].split("s:")[1].strip()
                    networks.add((ssid, mac))
        return networks

    def connect(self, ssid, password):
        """Connect self to a network

        #### Args:
            ssid (string): The SSID of the network
            password (string): The password for the network
        #### Returns:
            status (boolean): Connection Status (True=connected)
        """
        output = ""
        for _ in range(5):  # amount of retries
            try:
                output = subprocess.check_output(
                    "nmcli d wifi connect {} password {}".format(ssid, password), shell=True).decode("utf-8")
            except:
                continue
            else:
                break

        if "success" in output:
            return True
        else:
            return False

    def disconnect(self):
        """Disconnect self from network
        """
        for _ in range(5):  # number of retries
            try:
                output = subprocess.check_output(
                    "nmcli d disconnect {}".format(self.wifiInterface), shell=True)
                assert "success" in output
            except:
                continue
            else:
                break

    def connectClient(self, client):
        """Connect a client to the main network

        #### Args:
            client (dict): client data

        #### Returns:
            status (int): Status code of connection (1: success, 0: failure)
        """
        # TODO: implement api call to connect ESP to network
        pass

    def disconnectClient(self, client):
        """Disconnect a client from the main network to

        #### Args:
            client (dict): client data
        #### Returns:
            status (int): Status code of the disconnecting procedure (1: success, 0: failure)
        """
        # TODO : implement api call to disconnect ESP from network
        pass

    def queryNetworks(self, networks):
        """Query Wifi Networks for Microcontrollers

        #### Args:
            networks (list): list of networks to query

        #### Returns:
            networkData (dict): dict of networks and connected devices
        """
        # TODO: return dict of networks with containing devices
        networks = self.search()
        for network in networks:
            pass

    def getMicrocontrollerNetworks(self):
        """get nearby networks which are hosted by ESP8266's
        #### Returns:
            microcontrollerNetworks (list): list of networks hosted by the ESP8266's
        """
        available = self.search()
        networkData = self.queryNetworks(available)
        # TODO: get right networks out of networkData (dict)
        pass
