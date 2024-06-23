# 10_Files_Uploads/app.py 

from flask import Flask
app = Flask(__name__)


from flask import request

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['the_file']
        f.save('/var/www/uploads/uploaded_file.txt')



if __name__ == "__main__":
    app.run(debug=True)

