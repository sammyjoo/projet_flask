#source venv/bin/activate pour activé dans le terminal 
from appmeteo import app
if __name__ == "__main__":
    app.run(debug=True)