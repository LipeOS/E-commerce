Configuracao do DB

create table usuarios (
  id bigint primary key generated always as identity,
  nome_completo text not null,
  tipo_usuario text check (tipo_usuario in ('usuario', 'admin')) not null,
  senha text not null,
  confirmar_senha text not null
);