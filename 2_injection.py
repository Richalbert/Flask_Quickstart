# import Flask
from flask import Flask, request, render_template_string

# Create an instance of this class
app = Flask(__name__)

# Tell Flask what URL should trigger our function
@app.route('/')
def index():
    return '''
        <form method="post" action="/greet">
            Name: <input type="text" name="name">
            <input type="submit">
        </form>
    '''

@app.route('/greet', methods=['POST'])
def greet():
    name = request.form['name']
    # return render_template_string('<h1>Hello, {{ name }}</h1>', name=name)

    # Ajoutons du HTML supplémentaire pour forcer l'injection à être plus évidente
    return render_template_string('<h1>Hello, {{ name|safe }}</h1><p>Welcome to our site!</p>', name=name)
 


if __name__ == '__main__':
    app.run(debug=True)
    #app.run()


'''
    Saisir dans le champ name : <script>alert('Hacked!');</script>
'''