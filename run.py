#source venv/bin/activate pour activé dans le terminal
#python3 run.py 
#afficher l'URL sur le navigateur
#pip freeze > requirements.txt / pour exporter le venv
# pip install 

from appmeteo import app
if __name__ == "__main__":
    app.run(debug=True)