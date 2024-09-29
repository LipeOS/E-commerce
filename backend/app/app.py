from flask import Flask, render_template, request, jsonify, redirect, url_for
import mysql.connector
from mysql.connector import Error
import os

# Definindo o caminho correto para as pastas de templates e arquivos estáticos
app = Flask(
    __name__, 
    template_folder=os.path.join(os.path.dirname(__file__), '../../frontend/templates'), 
    static_folder=os.path.join(os.path.dirname(__file__), '../../frontend/static')
)

# Função para conectar ao banco de dados MySQL
def create_connection():
    try:
        connection = mysql.connector.connect(
            host='localhost',   # Endereço do servidor MySQL
            database='nome_do_banco',  # Nome do banco de dados
            user='seu_usuario',  # Usuário do banco de dados
            password='sua_senha'  # Senha do banco de dados
        )
        if connection.is_connected():
            print("Conexão com o MySQL estabelecida com sucesso")
            return connection
    except Error as e:
        print(f"Erro ao conectar ao MySQL: {e}")
        return None

# Rota para página de cadastro
@app.route('/')
def cadastro():
    return render_template('cadastro.html')

# Rota para página de login (GET)
@app.route('/login', methods=['GET'])
def login_page():
    return render_template('login.html')

# Rota para processar login (POST)
@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    # Simulação de autenticação (aqui você pode adicionar lógica para verificar no banco de dados)
    if username == "admin" and password == "senha123":
        # Redireciona para a página 'index.html' após login bem-sucedido
        return redirect(url_for('index'))
    else:
        return jsonify({"status": "error", "message": "Credenciais inválidas!"})

# Rota para a página principal (index.html)
@app.route('/index')
def index():
    return render_template('index.html')  # Renderiza a página 'index.html'

if __name__ == '__main__':
    app.run(debug=True)
