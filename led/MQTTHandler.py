from paho import mqtt
from paho.mqtt import mqtt_client
from os import getenv


class MQTTHandler:

    client_id = getenv("MQTT_CLIENT_ID")
    host = getenv("MQTT_BROKER")
    port = getenv("MQTT_BROKER_PORT")
    username = getenv("MQTT_BROKER_USERNAME")
    password = getenv("MQTT_BROKER_PASSWORD")

    def __init__(self):
        self.pub_client = mqtt_client.Client(self.client_id)
        self.pub_client.connect(self.host, self.port)
        self.sub_client = mqtt_client.Client()
        self.sub_client.connect(self.host, self.port)
        self.sub_client.subscribe("led/waiting")
        self.sub_client.on_message = self._handleDevices

    def _handleDevices(self, client, userdata, message) -> None:
        """handle an incoming message from a subscribed topic

        Parameters
        ----------
        client : [type]
            the client who receives the topic
        userdata : dict
            the data of the sending user
        message : str
            the message to handle
        """
        # Ask for Name for Device (maybe by using the cards designed for the old setup tab)
        pass

    def _connectDevice(self, name) -> None:
        """connect a device to the broker

        Parameters
        ----------
        name : str
            the name of the device
        """
        self.pub_client.publish("led/connect", str({"host": self.host, "port": self.port, "name": name}))

    def setRGB(self, client, r, g, b) -> None:
        """set the rgb values of a given client

        Parameters
        ----------
        client : str
            client name
        r : int
            r value of the color
        g : int
            g value of the color
        b : int
            b value of the color
        """
        self.pub_client.publish("led/{client}", str({"r": r, "g": g, "b": b}))

    def disconnect(self, name) -> None:
        """disconnect a client

        Parameters
        ----------
        name : str
            name of the client to disconnect
        """
        pass
