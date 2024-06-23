# 10_formulaire.py

# les imports
from flask import Flask, request, render_template

# l'instance de la classe
app = Flask(__name__)

# les routes
@app.route('/')
def index():
    return render_template('form.html')

@app.route('/hello', methods=['GET', 'POST'])
def hello():

    print(request)

    # la route provient de l'action du formulaire
    # les donnees se trouvent dans request.form
    if request.method == 'POST':
        name = request.form['name']
    else:
        # sinon c'est une requete GET 
        # la route provient de la saisie de l'url dans le navigateur
        # les donnees se trouvent dans request.args
        print(request.args) # http://localhost:5000/hello?name=foobar
        name = request.args.get('name', 'Saisissez votre nom a partir du formulaire ')
        print(name)
    return f'Hello, {name}!'


if __name__ == '__main__':
    app.run(debug=True)
