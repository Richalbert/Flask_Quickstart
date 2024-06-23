# 3_routing.py

# import Flask
from flask import Flask

# Create an instance of this class
app = Flask(__name__)

# Tell Flask what URL should trigger our function
@app.route('/')
def index():
    return '<h1>Welcome on Index Page</h1>'

@app.route('/hello')
def hello():
    return '<h1>Hello world !</h1>'

if __name__ == "__main__":
    app.run(debug=True)