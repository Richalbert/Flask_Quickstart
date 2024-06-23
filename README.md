# Flask_Quick_Start

d'apres le tuto : [Flask Quickstart](https://flask.palletsprojects.com/en/3.0.x/quickstart/)

# install

sur le Bureau : 
  - git clone https://github.com/Richalbert/Flask_Quick_Start.git
  - cd Flask_Quick_Start
  - python -m venv .venv
  - .venv\Scripts\activate
  - pip install flask
  - pip freeze > requirements.txt

# pour tester le programme

1. lancer le serveur de developpement Flask localement
    - flask --app .\1_hello.py run
2. avec le mode debug 
    - flask --app .\1_hello.py run --debug
3. se connecter au serveur via un navigateur
    - http://127.0.0.1:5000

## l'aide de Flask
![image](https://github.com/Richalbert/Flask_Quick_Start/assets/40654401/dba4d1b2-3947-4236-911b-245a514da4c1)


## Remarque:

- Flask cree des applications WSGI qui communiquent avec un serveur WSGI.
- Les requetes HTTP sont transformees en requetes WSGI. 
- [deployer un serveur WSGI](https://flask.palletsprojects.com/en/3.0.x/deploying/) en production

## autre facon de lancer le serveur

1. ajouter
   
     `if __name__ == "__main__ :`
            `app.run(debug=True)`
     
3. lancer
   
    `python hello.py`


# HTML Escaping

- idealement il faut proteger les donnees contre les attaques par injection
- par defaut le moteur Jinja2 e,peche les injections 
- pour tester les injections <script>alert('Hacked !');</script> 2 programmes 
  - 1bis_injection.py
  - !bis_no_injection.py

# Routing

- Flask utilise des decorateur rooute() pour associer l'URL a la fonction

# Variable Rules

- on peut passer une variables depuis l'URL avec <variable_name>
- la fonction a **variable_name** comme argument
  
# Unique URL

- Slash finale (/projects/) : Considéré comme un "dossier". Flask redirige /projects vers /projects/.
- Pas de slash finale (/about) : Considéré comme un "fichier". Flask retourne une erreur 404 pour /about/

# URL Building

- permet de generer des URLs de maniere dynamique
- **@app.route('/login')** declare la vue (fonction) **index()** pour la route **/login**

# HTTP Methods

- par defaut @app.route() repond aux requetes GET
- methods
  
# Static Files

# Rendering Templates

- permet de separer la logique (le code Pytho) de la presentation (le HTML)
- la fonction render_templates('hello.html', person=name) passe variable person au fichier templates/hello.html

# Logging

