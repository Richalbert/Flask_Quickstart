# Minimal App

# HTML Escpace contre les attaques par injection
from markupsafe import escape

# import Flask
from flask import Flask

# Create an instance of this class
app = Flask(__name__)

# Tell Flask what URL should trigger our function

@app.route("/<name>")
def hello(name):
    # message to display in browser
    # return "<p>Hello World</p>"
    return f"Hello , {name}"

@app.route("/")
def index():
    return "<h2>Coucou</h2>" 

if __name__ == "__main__":
    app.run(debug=True)
