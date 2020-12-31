from flask import render_template
from espwebsite import app


@app.route('/', methods=['GET'])
def base():
    return render_template("base.html")
