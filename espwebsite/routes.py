from flask import render_template
from espwebsite import app, config, helpers


@ app.route('/', methods=['GET'])
def base():
    return render_template("base.html", controllers=helpers.getControllersHTML(config.get('activeControllers')))


@ app.route('/controls', methods=['GET'])
def controls():
    return helpers.getControllersHTML(config.get('activeControllers'))


@ app.route('/setup', methods=['GET'])
def setup():
    return open("espwebsite/templates/setup.html").read()


@ app.route('/network', methods=['GET'])
def network():
    return open("espwebsite/templates/network.html").read()
