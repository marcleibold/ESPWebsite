from paho import mqtt
from paho.mqtt import mqtt_client
from .config import *

client_id = Config.get("MQTT.client_id")
broker = Config.get("MQTT.broker")
port = Config.get("MQTT.port")
username = Config.get("MQTT.username")
password = Config.get("MQTT.password")


def connect() -> mqtt_client.Client:
    """connect to MQTT broker
    """
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)
    # client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client


def publish(client, topic, payload) -> None:
    """publish a message to a give topic

    Parameters
    ----------
    client : [type]
        the client to publish a topic
    topic : str
        the topic to push the message to
    payload : str
        the payload/message to push
    """
    client.publish(topic, payload)


def subscribe(client, topic) -> None:
    """subscribe to a given topic

    Parameters
    ----------
    client : [type]
        the client which subscribes
    topic : str
        the topic to subscribe to
    """
    client.subscribe(topic)
    client.on_message = handleMessage
    client.loop_forever()


def disconnect(client) -> None:
    """disconnect the client

    Parameters
    ----------
    client : [type]
        the client to disconnect
    """
    client.disconnect()

# callbacks


def handleMessage(client, userdata, message) -> None:
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
    print(f"message received: {message} - from {client} with {userdata}")
