import os
from flask import Flask, render_template, request, redirect, url_for, session, send_from_directory, jsonify
from werkzeug.utils import secure_filename
import mysql.connector
from mysql.connector import Error
from werkzeug.security import generate_password_hash, check_password_hash

# Configuração do diretório para armazenar uploads
UPLOAD_FOLDER = os.path.join(os.path.dirname(__file__), '../../frontend/static/uploads')
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

app = Flask(
    __name__, 
    template_folder=os.path.join(os.path.dirname(__file__), '../../frontend/templates'), 
    static_folder=os.path.join(os.path.dirname(__file__), '../../frontend/static')
)

# Chave secreta para criptografar as sessões
app.secret_key = 'sua_chave_secreta_aqui'

# Configuração da pasta de upload
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

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

# Função para verificar se o arquivo tem uma extensão permitida
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/carrinho')
def carrinho():
    if not session.get('logged_in'):
        return redirect(url_for('login_page'))

    connection = create_connection()
    cursor = connection.cursor(dictionary=True)

    usuario_id = session['username']  # Ajuste se necessário
    cursor.execute("SELECT * FROM carrinho WHERE usuario_id = %s", (usuario_id,))
    cart_items = cursor.fetchall()

    return render_template('carrinho.html', cart_items=cart_items)
    


@app.route('/produto/<int:produto_id>')
def produto_detalhes(produto_id):
    # Conectar ao banco de dados
    connection = create_connection()
    cursor = connection.cursor(dictionary=True)

    # Buscar informações do produto específico pelo ID
    cursor.execute("SELECT * FROM produtos WHERE id = %s", (produto_id,))
    produto = cursor.fetchone()

    # Verifica se o produto foi encontrado
    if not produto:
        return "Produto não encontrado", 404

    return render_template('detalhespro.html', produto=produto)



# Rota para página de cadastro
@app.route('/')
def cadastro():
    return render_template('cadastro.html')

# Rota para página de cadastro (GET) e processamento do cadastro (POST)
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        fullname = request.form['fullname']
        role = request.form['role']  # Recebe o tipo de usuário (admin ou user)
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

        # Redireciona baseado no tipo de usuário
        if role == 'admin':
            return redirect(url_for('admin_dashboard'))  # Redireciona para a página de administração se for admin
        else:
            return redirect(url_for('login_page'))  # Redireciona para a página de login se for user

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

# Rota para cadastrar novos produtos com upload de imagem
@app.route('/register_product', methods=['POST'])
def register_product():
    product_name = request.form['product_name']
    purchase_price = float(request.form['purchase_price'])
    sale_price = float(request.form['sale_price'])
    quantity = int(request.form['quantity'])
    description = request.form['description']
    file = request.files['image_file']

    # Verificando se o arquivo é permitido
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)

        # Verificando e criando o diretório de uploads, caso não exista
        if not os.path.exists(app.config['UPLOAD_FOLDER']):
            os.makedirs(app.config['UPLOAD_FOLDER'])

        # Caminho completo do arquivo
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)  # Salvando o arquivo no diretório de uploads
        
        # Salvando o caminho da imagem no banco de dados (apenas o nome do arquivo)
        image_url = f"uploads/{filename}"
    else:
        return jsonify({"status": "error", "message": "Arquivo de imagem inválido"})

    connection = create_connection()
    cursor = connection.cursor()

    # Inserindo novo produto no banco com os novos campos (descrição e imagem)
    insert_query = """
    INSERT INTO produtos (nome_produto, preco_compra, preco_venda, quantidade, descricao, imagem_url)
    VALUES (%s, %s, %s, %s, %s, %s)
    """
    cursor.execute(insert_query, (product_name, purchase_price, sale_price, quantity, description, image_url))
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

# Rota para servir arquivos de imagem
@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

@app.route('/adicionar_ao_carrinho/<int:produto_id>', methods=['POST'])
def adicionar_ao_carrinho(produto_id):
    if not session.get('logged_in'):
        return jsonify({"status": "error", "message": "Usuário não logado!"})

    usuario_id = session['username']  # Ajuste se necessário

    connection = create_connection()
    cursor = connection.cursor()

    # Verifique se o produto já está no carrinho
    cursor.execute("SELECT * FROM carrinho WHERE usuario_id = %s AND produto_id = %s", (usuario_id, produto_id))
    item_existente = cursor.fetchone()

    if item_existente:
        # Se já existe, atualiza a quantidade
        nova_quantidade = item_existente['quantidade'] + 1
        cursor.execute("UPDATE carrinho SET quantidade = %s WHERE usuario_id = %s AND produto_id = %s",
                       (nova_quantidade, usuario_id, produto_id))
    else:
        # Se não existe, adiciona ao carrinho
        cursor.execute("INSERT INTO carrinho (usuario_id, produto_id, quantidade) VALUES (%s, %s, %s)",
                       (usuario_id, produto_id, 1))

    connection.commit()
    cursor.close()
    connection.close()

    return jsonify({"status": "success", "message": "Produto adicionado ao carrinho!"})


if __name__ == '__main__':
    app.run(debug=True)
