# 10_Files_Uploads/app.py 

from flask import Flask, request, redirect, url_for, render_template
import os

# Configuration de l'application Flask
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads' # Dossier ou les fichiers telecharges seront stocke
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # Limite de taille de fichier à 16 MB

print(app)

# Route pour la page d'accueil avec le formulaire de téléchargement
@app.route('/')
def index():
    return render_template('upload.html')

# Route pour gérer le téléchargement de fichiers
@app.route('/upload', methods=['POST'])
def upload_file():

    # verification de la presence du fichier a telecharger
    # request.files est un dictionnaire qui contient tous les fichiers 
    # envoyes par le formulaire, dont les cles sont les noms de fichier
    if 'file' not in request.files:
        return 'No file'
    
    file = request.files['file']
    
    # verification que le fichier a un nom
    if file.filename == '':
        return 'No selected file'
    
    # enregistrement du fichier dans le dossier UPLOAD_FOLDER
    if file:
        filename = file.filename
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        print(f'File {filename} successfully uploaded')
        return render_template("acknowledgement.html", name=filename, multilpe=None)
    
    return 'Failed to upload file'


@app.route('/uploads', methods=['POST'])
def uploads_file():
    # request.files est un dictionnaire qui contient tous les fichiers 
    # envoyes par le formulaire, dont les cles sont les noms de fichier

    # verifie que le formulaire contient un champ de fichier
    if 'file' not in request.files:
        return 'No file'
    
    # request.files['file'] est une liste contenant plusieurs fichiers
    #print("==> ", request.files)

    # permet d'obtenir une liste des fichiers telecharges
    files = request.files.getlist('file')
    #print("==> ", files)

    # verifie que l'utilisateur a selectionne un champ de fichier
    if not files or files[0].filename == '':
        return 'No selected file'
    
    # sauvegarde de chaque fichier de la liste
    filename_list = []
    for file in files:
        if file and file.filename:
            filename = file.filename
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            print(f'File {filename} successfully uploaded')
            filename_list.append(filename)
    
    print('All files successfully uploaded')
    return render_template("acknowledgement.html", name=filename_list, multilpe="OUI")





@app.route('/upload2', methods=['POST'])
def upload2_file():
    if 'file' not in request.files:
        return 'No file'
    
    files = request.files.getlist('file')
    
    if not files or files[0].filename == '':
        return 'No selected file'
    
    filenames = []
    for file in files:
        if file and file.filename:
            filename = file.filename
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            filenames.append(filename)
    
    multiple = 'OUI' if len(filenames) > 1 else None
    return render_template('result.html', multiple=multiple, filenames=filenames)


# Lancement de l'application Flask
if __name__ == '__main__':
    app.run(debug=True)





# from flask import Flask
# app = Flask(__name__)


# # from flask import request

# # @app.route('/upload', methods=['GET', 'POST'])
# # def upload_file():
# #     if request.method == 'POST':
# #         f = request.files['the_file']
# #         f.save('/var/www/uploads/uploaded_file.txt')



# if __name__ == "__main__":
#     app.run(debug=True)

