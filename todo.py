from flask import Flask, render_template, url_for

app = Flask(__name__)


class Tarefa:
    def __init__(self, nome, prazo):
        self.nome = nome
        self.prazo = prazo

tarefas = []

@app.route('/')
def index():
    return render_template('index.html')


app.run(debug=True)
