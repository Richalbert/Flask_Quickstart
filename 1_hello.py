# Minimal App

# import Flask
from flask import Flask

# Create an instance of this class
app = Flask(__name__)

# Tell Flask what URL should trigger our function
@app.route("/")
def hello_world():
    # message to display in browser
    return "<p>Hello World</p>"

