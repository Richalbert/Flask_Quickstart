# 6_URL_Building.py

# import Flask, 
from flask import Flask
from flask import url_for

#import HTML Escape
from markupsafe import escape

# Create an instance of this class
app = Flask(__name__)


# declare la vue 'index' pour la route '/'
@app.route('/')
def index():
    return 'index'

# declare la vue 'login' pour la route '/login'
@app.route('/login')
def login():
    return 'login'

# declare la vue 'profile' pour la route '/user/<username>'
@app.route('/user/<username>')
def profile(username):
    return f'{username}\'s profile'



with app.test_request_context():

    # url_for('index') genere l'URL '/' pour la vue 'index()' 
    print(url_for('index'))

    # url_for('login') genere l'URL '/login' pour la vue 'login()' 
    print(url_for('login'))

    # url_for('login', next='/') genere l'URL '/login?next=/' pour la vue 'login()' 
    print(url_for('login', next='/'))

    # url_for('profile', username='John Doe') genere l'URL '/user/John Doe' pour la vue profile() avec le parametre dynamique 'username'
    #print(url_for('profile', username='John Doe'))



if __name__ == "__main__":
    app.run(debug=True)