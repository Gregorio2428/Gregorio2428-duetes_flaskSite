from flask import Flask
from markupsafe import escape

app = Flask(__name__)

@app.route("/hello")
@app.route("/hello/")
@app.route("/hello/<user_name>")
def hello(user_name=None):

    if user_name:
        return f"<h1>Hi, {escape(user_name)}!</h1>"
    else:
        return "<h1>Hi, World!</h1>"

