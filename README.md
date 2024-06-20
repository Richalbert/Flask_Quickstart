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

1. lancer le serveur Flask localement
    - flask --app .\1_hello.py run
2. se connecter au serveur via un navigateur
    - http://127.0.0.1:5000

# l'aide de Flask
![image](https://github.com/Richalbert/Flask_Quick_Start/assets/40654401/dba4d1b2-3947-4236-911b-245a514da4c1)


*REMARQUE :*

- Flask cree des applications WSGI qui communiquent avec un serveur WSGI.
- Les requetes HTTP sont transformees en requetes WSGI. 
- [deployer un serveur WSGI](https://flask.palletsprojects.com/en/3.0.x/deploying/) en production
