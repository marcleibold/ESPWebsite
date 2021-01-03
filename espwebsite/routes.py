from flask import render_template
from espwebsite import app, config, helpers


@ app.route('/', methods=['GET'])
def base():
    return render_template("base.html", controllers=helpers.getControllersHTML(config.get('activeControllers')))
