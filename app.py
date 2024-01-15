1. 
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Récupérez les données du formulaire
        nom = request.form['nom']
        prenom = request.form['prenom']
        # Faites quelque chose avec les données (par exemple, imprimez-les)
        print(f"Nom: {nom}, Prénom: {prenom}")

    # Renvoie la page HTML avec le formulaire
    return render_template('formulaire.html')

if __name__ == '__main__':
    app.run(debug=True)




