# 7_http_methods.py

# import Flask
from flask import Flask

# import request
from flask import request

# Create an instance of this class
app = Flask(__name__)


# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         return do_the_login()
#     else:
#         return show_the_login_form()


@app.get('/login')
def login_get():
    return show_the_login_form()

@app.post('/login')
def login_post():
    return do_the_login()
