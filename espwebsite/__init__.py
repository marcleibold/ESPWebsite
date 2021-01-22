from flask import Flask
import os
import json
from espwebsite import config

if "config.json" not in os.listdir():
    with open("config.json", "a") as f:
        json.dump(config.getDefault(), f)

config.load()

app = Flask(__name__)
