from flask import Flask, url_for

app = Flask(__name__)

@app.route('/')
def index():
    # Génère un lien vers la page de profil de John Doe
    profile_url = url_for('profile', username='John Doe')
    return f'<a href="{profile_url}">Go to John Doe\'s profile</a>'

@app.route('/login')
def login():
    return 'login'

@app.route('/user/<username>')
def profile(username):
    return f"{username}'s profile"

if __name__ == '__main__':
    app.run(debug=True)
