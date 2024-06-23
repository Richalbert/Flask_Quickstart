# 8_rendering_templates.py

# import Flask, render_template
from flask import Flask, render_template

# Create an instance of this class
app = Flask(__name__)


@app.route('/hello')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', person=name)



if __name__ == '__main__':
    app.run(debug=True)
