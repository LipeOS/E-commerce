# Projeto de Banco de Dados

Este projeto cria um banco de dados chamado `banco` com duas tabelas: `usuarios` e `produtos`.

## Criação do Banco de Dados

Para criar o banco de dados, execute o seguinte comando SQL:

```sql

-- Criação do Banco de Dados
CREATE DATABASE banco;

-- Selecionando o Banco de Dados
USE banco;

-- Criação da tabela 'usuarios'
CREATE TABLE usuarios (
  id BIGINT PRIMARY KEY AUTO_INCREMENT,         -- Identificador único do usuário
  nome_completo TEXT NOT NULL,                  -- Nome completo do usuário
  tipo_usuario ENUM('user', 'admin') NOT NULL, -- Tipo de usuário (pode ser 'user' ou 'admin')
  senha TEXT NOT NULL                           -- Senha do usuário
);

-- Criação da tabela 'produtos'
CREATE TABLE produtos (
  id BIGINT PRIMARY KEY AUTO_INCREMENT,         -- Identificador único do produto
  nome_produto TEXT NOT NULL,                   -- Nome do produto
  preco_compra DECIMAL(10, 2) NOT NULL,        -- Preço de compra do produto
  preco_venda DECIMAL(10, 2) NOT NULL,         -- Preço de venda do produto
  quantidade INT NOT NULL,                      -- Quantidade disponível do produto
  descricao TEXT,                               -- Descrição do produto
  imagem_url VARCHAR(255)                       -- URL da imagem do produto
);

-- Criação da tabela 'carrinho'
CREATE TABLE carrinho (
    id INT AUTO_INCREMENT PRIMARY KEY,
    usuario_id BIGINT,  -- Referência ao usuário logado
    produto_id BIGINT,  -- Referência ao ID do produto
    quantidade INT,
    preco_venda DECIMAL(10, 2),
    total_preco DECIMAL(10, 2),
    imagem_url TEXT,
    FOREIGN KEY (usuario_id) REFERENCES usuarios(id),  -- Chave estrangeira referenciando a tabela usuarios
    FOREIGN KEY (produto_id) REFERENCES produtos(id)   -- Chave estrangeira referenciando a tabela produtos
);


```sql


