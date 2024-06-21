# 5_Unique_URLs.py

# import Flask
from flask import Flask

#import HTML Escape
from markupsafe import escape


# Create an instance of this class
app = Flask(__name__)


# Tell Flask what URL should trigger our function

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return f'User {escape(username)}'


@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return f'Post {post_id}'


@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return f'Subpath: {escape(subpath)}'


# The canonical URL with slash
@app.route('/projects/')
def projects():
    return "<h1>The project page</h1>"

# The slash 
@app.route('/about')
def about():
    return "<h1>The about page</h1>"


if __name__ == "__main__":
    app.run(debug=True)
