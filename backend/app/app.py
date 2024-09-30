from flask import Flask, render_template, request, jsonify, redirect, url_for
import mysql.connector
from mysql.connector import Error
import os
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(
    __name__, 
    template_folder=os.path.join(os.path.dirname(__file__), '../../frontend/templates'), 
    static_folder=os.path.join(os.path.dirname(__file__), '../../frontend/static')
)

# Função para conectar ao banco de dados MySQL
def create_connection():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='banco',
            user='seu_usuario',
            password='sua_senha'
        )
        if connection.is_connected():
            print("Conexão com o MySQL estabelecida com sucesso")
            return connection
    except Error as e:
        print(f"Erro ao conectar ao MySQL: {e}")
        return None

# Rota para o cadastro (GET e POST)
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        fullname = request.form['fullname']
        role = request.form['role']
        password = request.form['password']
        confirm_password = request.form['confirm_password']

        # Verificação de senha
        if password != confirm_password:
            return jsonify({"status": "error", "message": "As senhas não correspondem!"})

        connection = create_connection()
        if not connection:
            return jsonify({"status": "error", "message": "Erro de conexão com o banco de dados"})

        cursor = connection.cursor()

        # Verificação se o usuário já existe
        cursor.execute("SELECT * FROM usuarios WHERE nome_completo = %s", (fullname,))
        user_exists = cursor.fetchone()
        
        if user_exists:
            return jsonify({"status": "error", "message": "Usuário já cadastrado!"})

        # Hashing da senha
        hashed_password = generate_password_hash(password)

        # Inserção do novo usuário
        insert_query = "INSERT INTO usuarios (nome_completo, tipo_usuario, senha) VALUES (%s, %s, %s)"
        cursor.execute(insert_query, (fullname, role, hashed_password))
        connection.commit()

        return jsonify({"status": "success", "message": "Usuário cadastrado com sucesso!"})

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

    connection = create_connection()
    if not connection:
        return jsonify({"status": "error", "message": "Erro de conexão com o banco de dados"})

    cursor = connection.cursor()
    cursor.execute("SELECT * FROM usuarios WHERE nome_completo = %s", (username,))
    user = cursor.fetchone()

    if user and check_password_hash(user[3], password):  # user[3] é a senha armazenada no banco
        return redirect(url_for('index'))
    else:
        return jsonify({"status": "error", "message": "Credenciais inválidas!"})

# Rota para a página principal (index.html)
@app.route('/index')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
