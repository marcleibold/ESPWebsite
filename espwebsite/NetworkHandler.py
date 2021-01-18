import netifaces
import subprocess
import re
import os
import time
import dotenv


class NetworkHandler:

    wifiInterface = ""
    ethInterface = ""

    def __init__(self):
        dotenv.load_dotenv(dotenv_path=".")
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
            return False
        networks_raw = re.split("Cell\ [0-9]{2}\ -\ ", output)
        networks = set()
        for network in networks_raw:
            parts = re.split("\s{2,}", network)
            if len(parts) > 1:
                if len(parts[0]) > 0:
                    ssid = parts[1].split("ID:")[1].strip().strip('"')
                    networks.add(ssid)
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
                    "nmcli d wifi connect '{}' password '{}'".format(ssid, password), shell=True).decode("utf-8")
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
                assert "success" in output.decode("utf-8")
            except:
                continue
            else:
                break

    def connectClient(self, client):
        """Connect a client to the main network

        #### Args:
            client (dict): client data

        #### Returns:
            status (boolean): Status of connection (True: success, False: failure)
        """
        mac = client["mac"]
        espNetworks = self.getMicrocontrollerNetworks()
        clientSSID = "{}_network".format(mac)

        if clientSSID not in espNetworks:
            return False

        connected = self.connect(clientSSID, "espdefault")

        if not connected:
            return False

        creds = {
            "ssid": os.getenv("WIFI_SSID"),
            "pass": os.getenv("WIFI_PASS")
        }

        cmd = 'curl -XPUT http://192.168.4.1:8080/connect -d "{}" -v -m 2'.format(
            str(creds))
        print(cmd)
        try:
            output = subprocess.check_output(cmd, shell=True)
        except subprocess.CalledProcessError as e:
            if "28" in str(e):
                self.disconnect()
                return True
        else:
            return False

    def disconnectClient(self, client):
        """Disconnect a client from the main network to

        #### Args:
            client (dict): client data
        #### Returns:
            status (boolean): Status of the disconnecting procedure (True: success, False: failure)
        """

        if self.connect(os.getenv("WIFI_SSID"), os.getenv("WIFI_PASS")):

            cmd = "curl -XPUT http://{}:8080/disconnect -v -m 2".format(
                client["ip"])
            try:
                output = subprocess.check_output(cmd, shell=True)
            except subprocess.CalledProcessError as e:
                if "28" in str(e):
                    return True
            else:
                return False
        else:
            return False

    def getMicrocontrollerNetworks(self):
        """Query Wifi Networks for Microcontrollers

        #### Args:
            networks (list): list of networks to query

        #### Returns:
            espNetworks (list): list of ESP networks
        """
        pattern = re.compile(
            "([0-9A-Fa-f]{2}\:){5}([0-9A-Fa-f]{2})_network")  # regex pattern for ESP network SSID
        networks = self.search()
        if networks == False:
            return set()
        espNetworks = set()
        for network in networks:
            if pattern.match(network):
                espNetworks.add(network)
        return espNetworks
