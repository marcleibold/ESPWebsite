from wifi import Cell
import netifaces


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
        """
        wifiNetworks = Cell.all(self.wifiInterface)
        return wifiNetworks

    def connect(self, client):
        """Connect a client to the main network

        Args:
            client (dict): client data
        """
        # TODO: implement api call to connect ESP to wifi
        pass

    def queryNetworks(self, networks):
        """Query Wifi Networks for Microcontrollers

        Args:
            networks (list): list of networks to query
        """
        # TODO: return dict of networks with containing devices
        pass

    def getMicrocontrollerNetworks(self):
        """get nearby networks which are hosted by ESP8266's
        """
        available = self.search()
        networkData = self.queryNetworks(available)
        # TODO: get right networks out of networkData (dict)
        pass
