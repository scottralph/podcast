import os

from flask import Flask
from flask import Flask, request, send_from_directory

app = Flask(__name__)

@app.route('/static/<path>')
def send_static(path):
    return send_from_directory('static', path)


@app.route("/")
def hello_world():
    name = os.environ.get("NAME", "World")
    return "Hello {}!".format(name)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))