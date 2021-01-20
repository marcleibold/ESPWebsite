from flask import render_template, jsonify, Response, request
from espwebsite import app, config, helpers
import json


@ app.route('/', methods=['GET'])
def base():
    return render_template("base.html")


@ app.route('/controls', methods=['GET'])
def controls():
    # return helpers.getControllersHTML(config.get('connectedDevices'))
    return open("espwebsite/templates/controls.html").read()


@ app.route('/setup', methods=['GET'])
def setup():
    return open("espwebsite/templates/setup.html").read()


@ app.route('/waiting', methods=['GET'])
def getWaitingDevices():
    return jsonify(helpers.getWaitingDevices())


@ app.route('/network', methods=['GET'])
def network():
    return open("espwebsite/templates/network.html").read()


@ app.route('/connect', methods=['PUT'])
def connect():
    data = request.get_json(force=True)
    if data:
        status = helpers.connect(data)
        response = json.dumps(data)
        if status == 1:
            return Response(response, status=201)
        else:
            return Response(status=409)
    else:
        return Response(status=409)


@ app.route('/connected', methods=['GET'])
def getConnectedDevices():
    return jsonify(config.get("connectedDevices"))


@ app.route('/disconnect', methods=['POST'])
def disconnect():
    data = request.get_json(force=True)
    if data:
        status = helpers.disconnect(data)
        if status == 1:
            return Response(status=200)
        else:
            return Response(status=409)
    else:
        return Response(status=409)


@ app.route('/updateDevices', methods=['POST'])
def update():
    helpers.updateConnected()
    return Response(status=200)
