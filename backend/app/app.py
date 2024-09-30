from flask import Flask, render_template, request, jsonify, redirect, url_for, session
import mysql.connector
from mysql.connector import Error
import os
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(
    __name__, 
    template_folder=os.path.join(os.path.dirname(__file__), '../../frontend/templates'), 
    static_folder=os.path.join(os.path.dirname(__file__), '../../frontend/static')
)

# Chave secreta para criptografar as sessões
app.secret_key = 'sua_chave_secreta_aqui'

# Função para conectar ao banco de dados MySQL
def create_connection():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='banco',
            user='root',
            password='1234'
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

# Rota para página de cadastro (GET) e processamento do cadastro (POST)
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        fullname = request.form['fullname']
        role = request.form['role']
        password = request.form['password']
        confirm_password = request.form['confirm_password']

        # Verifica se as senhas correspondem
        if password != confirm_password:
            return jsonify({"status": "error", "message": "As senhas não correspondem!"})

        # Criação de conexão com o banco
        connection = create_connection()
        if not connection:
            return jsonify({"status": "error", "message": "Erro de conexão com o banco de dados"})

        cursor = connection.cursor()

        # Verifica se o usuário já existe
        cursor.execute("SELECT * FROM usuarios WHERE nome_completo = %s", (fullname,))
        user_exists = cursor.fetchone()
        
        if user_exists:
            return jsonify({"status": "error", "message": "Usuário já cadastrado!"})

        # Gera hash da senha
        hashed_password = generate_password_hash(password)

        # Insere novo usuário no banco de dados
        insert_query = "INSERT INTO usuarios (nome_completo, tipo_usuario, senha) VALUES (%s, %s, %s)"
        cursor.execute(insert_query, (fullname, role, hashed_password))
        connection.commit()

        # Fecha a conexão
        cursor.close()
        connection.close()

        return redirect(url_for('admin_dashboard'))

    return render_template('cadastro.html')

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
        # Criação da sessão para o usuário logado
        session['logged_in'] = True
        session['username'] = username
        session['role'] = user[2]  # user[2] é o tipo de usuário (user/admin)

        # Redireciona para a página de administração se for admin
        if user[2] == 'admin':
            return redirect(url_for('admin_dashboard'))
        else:
            return redirect(url_for('index'))
    else:
        return jsonify({"status": "error", "message": "Credenciais inválidas!"})

# Rota para a página principal (index.html) com lista de produtos
@app.route('/index')
def index():
    # Verificação se o usuário está logado
    if not session.get('logged_in'):
        return redirect(url_for('login_page'))  # Redireciona para a página de login se não estiver logado

    connection = create_connection()
    cursor = connection.cursor(dictionary=True)

    # Buscando todos os produtos para exibir na página principal
    cursor.execute("SELECT * FROM produtos")
    produtos = cursor.fetchall()

    return render_template('index.html', produtos=produtos)

# Rota para a página de administração
@app.route('/admin')
def admin_dashboard():
    # Verificação se o usuário é um admin
    if not session.get('logged_in') or session.get('role') != 'admin':
        return redirect(url_for('login_page'))  # Redireciona se não for admin ou não estiver logado

    connection = create_connection()
    cursor = connection.cursor(dictionary=True)

    # Buscando todos os produtos para exibir na aba de administração
    cursor.execute("SELECT * FROM produtos")
    produtos = cursor.fetchall()

    # Calculando o lucro de cada produto
    for produto in produtos:
        produto['lucro_unitario'] = produto['preco_venda'] - produto['preco_compra']
        produto['lucro_total'] = produto['lucro_unitario'] * produto['quantidade']

    return render_template('admin_dashboard.html', produtos=produtos)

# Rota para cadastrar novos produtos
@app.route('/register_product', methods=['POST'])
def register_product():
    product_name = request.form['product_name']
    purchase_price = float(request.form['purchase_price'])
    sale_price = float(request.form['sale_price'])
    quantity = int(request.form['quantity'])

    connection = create_connection()
    cursor = connection.cursor()

    # Inserindo novo produto no banco
    insert_query = """
    INSERT INTO produtos (nome_produto, preco_compra, preco_venda, quantidade)
    VALUES (%s, %s, %s, %s)
    """
    cursor.execute(insert_query, (product_name, purchase_price, sale_price, quantity))
    connection.commit()

    return redirect(url_for('admin_dashboard'))

# Rota para logout
@app.route('/logout')
def logout():
    # Remove as informações da sessão
    session.pop('logged_in', None)
    session.pop('username', None)
    session.pop('role', None)
    return redirect(url_for('login_page'))  # Redireciona para a página de login

# Rota para página de login (GET)
@app.route('/login', methods=['GET'])
def login_page():
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)
