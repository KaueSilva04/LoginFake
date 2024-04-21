import sqlite3
from flask import Flask, request, render_template




app = Flask(__name__)

from flask import Flask, render_template

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def save_user():
    # Acesse os dados do formulário
    usuario = request.form['username']
    senha = request.form['senha']

    # Conecte ao banco de dados
    conn = get_db_connection()

    if usuario == "opa" and senha == "1234":
        return exibir_dados()

    # Prepare a consulta SQL para inserir os dados
    sql = "INSERT INTO login (usuario, senha) VALUES (?, ?)"
    cursor = conn.cursor()
    cursor.execute(sql, (usuario, senha))

    # Salve as alterações no banco de dados
    conn.commit()

    # Feche a conexão
    conn.close()

    # Envie uma mensagem de sucesso (opcional)
    return render_template('index.html', message="Usuário cadastrado com sucesso!")

@app.route('/exibir_dados')
def exibir_dados():
    # Conecte ao banco de dados
    conn = get_db_connection()

    # Execute a consulta SQL para recuperar os dados do SELECT
    sql = "SELECT * FROM login"  # Selecione todas as colunas da tabela login
    cursor = conn.cursor()
    cursor.execute(sql)

   

    # Envie os dados para o template HTML
    dados = cursor.fetchall()  # Obtém todos os resultados da consulta
    # Feche a conexão com o banco de dados
    conn.close()
    return render_template('exibir_dados.html', dados=dados)

if __name__ == '__main__':
    app.run(debug=True)
