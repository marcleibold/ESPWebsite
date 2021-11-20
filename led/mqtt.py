import paho.mqtt.client as mqtt
from dotenv import load_dotenv
from os import getenv
from led.models import Controller
import json

load_dotenv()


def handle_connection(data):
    # TODO: duplicate checking
    data = json.loads(data)
    new = Controller(name=data["name"])
    new.save()


def on_connect(client, userdata, rc, properties=None):
    # TODO: handle on_connect
    client.subscribe("led/connect")


def on_message(client, userdata, msg):
    data = msg.payload.decode("utf-8")
    if msg.topic == "led/connect":
        handle_connection(data)


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(getenv("MQTT_BROKER_HOST"), int(getenv("MQTT_BROKER_PORT")), 60)
