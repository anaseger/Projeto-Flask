from flask import Flask, render_template
app = Flask(__name__)  # iniciando classe flask

# endereço do site
@app.route('/')  # rota principal
@app.route('/index')  # rota alternativa
def index():
    #return "Hello World"
    nome='Ana'
    dados={"profissão":"SRE", "cidade":"Santa Rosa"}
    return render_template('index.html', nome=nome,dados=dados)
