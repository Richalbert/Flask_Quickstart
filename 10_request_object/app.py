# app.py 

# les imports
from flask import Flask, request, render_template

# l'instance de la classe
app = Flask(__name__)

# les routes
@app.route('/')
def index():
    return render_template('form.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    login = None
    password = None

    if request.method == 'POST':
        # Les donnees sont dans request.form
        login = request.form['login']
        password = request.form['password']
        if not login or not password:
            error = 'Invalid login / password'
        else:
            # affichage dans la console
            print(login)
            print(password)
    else:
        # Les donnees sont dans request.args
        error = 'Invalid login / password'
        print(error)

    # On appelle la vue login.html avec 3 variables
    return render_template('login.html', login=login, password=password, error=error)


if __name__ == '__main__':
    app.run(debug=True)