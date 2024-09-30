CREATE TABLE usuarios (
  id BIGINT PRIMARY KEY AUTO_INCREMENT,
  nome_completo TEXT NOT NULL,
  tipo_usuario ENUM('user', 'admin') NOT NULL,
  senha TEXT NOT NULL
);

CREATE TABLE produtos (
    id BIGINT PRIMARY KEY AUTO_INCREMENT,
    nome_produto TEXT NOT NULL,
    preco_compra DECIMAL(10, 2) NOT NULL,
    preco_venda DECIMAL(10, 2) NOT NULL,
    quantidade INT NOT NULL
);
