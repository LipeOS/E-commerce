CREATE TABLE usuarios (
  id BIGINT PRIMARY KEY AUTO_INCREMENT,
  nome_completo TEXT NOT NULL,
  tipo_usuario ENUM('user', 'admin') NOT NULL,
  senha TEXT NOT NULL
);
