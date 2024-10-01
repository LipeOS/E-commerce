# Projeto - Desenvolvimento de um Sistema Empresarial de E-commerce

## Introdução
No dia 25/09/2024, os alunos do 3° NI da Escola Cesário Carlos de Almeida deram início ao Desenvolvimento de um Sistema Empresarial de E-commerce. O projeto consiste em desenvolver um sistema de e-commerce completo, onde a sala será dividida em setores de Design, Front-end, Back-end e Testers/Documentação. Cada grupo terá um papel fundamental no sucesso deste projeto.

## Objetivo
O objetivo deste projeto é criar um Sistema Empresarial de E-commerce completo (Ecommerce), onde a colaboração entre os setores de Design, Front-end, Back-end e Testers/Documentação será fundamental. Cada grupo terá um papel importante, contribuindo para o sucesso do sistema.

- O **Design** e o **Front-end** trabalharão juntos para desenvolver uma interface atraente e fácil de usar, garantindo que a navegação e as compras sejam uma experiência agradável para os usuários.
- O **Back-end** cuidará da lógica por trás do sistema, gerenciando produtos, processando pagamentos e controlando o estoque de forma segura e eficiente.

## Setores

### Setor 1 – Design
**Função:** Responsável pela identidade visual, layout das páginas, design responsivo e usabilidade do sistema.

**Integrantes:**
- Luana Vitória Cardia de Oliveira
- Camilly Silva Bertelini
- Sarah de Jesus Silva
- Emanuelly Victória Lino de Lale

### Setor 2 - Front-end
**Função:** Responsável pela criação da interface do usuário, implementação das páginas do site e integração com o Back-end.

**Integrantes:**
- Otávio de Souza Bernardes
- João Victor da Silva Vieira 
- Kauê Amatuzi Pinto
- Luiz Otávio Amaral Souza 
- Leone Gabriel Mariano

### Setor 3 – Back-end
**Função:** Focado na lógica do sistema, gerência de banco de dados com MySQLConnector, e implementação de rotas e APIs para comunicação com o Front-end.

**Integrantes:**
- Felipe Oliveira Silva
- Thulio Gomes da Silva
- Guilherme Arlindo Dantas da Silva
- João Vitor Jacó Belmiro

### Setor 4 – Testers / Documentação
**Função:** Focado em documentar e testar o sistema, identificar bugs, garantir que as funcionalidades estejam funcionando conforme esperado e que a experiência do usuário seja eficiente.

**Integrantes:**
- Larissa Viana Pereira
- Luana Aparecida Martini 
- Thiago de Freitas Araujo

## Prévia dos Setores

- **Setor 1 – Design:** O design espera a entrega de um projeto semelhante ao que a equipe planejou por meio do Figma.
- **Setor 2 – Front-end:** O Front-end espera implementar os planos de Design com eficácia, garantindo a máxima fidelidade ao projeto.
- **Setor 3 – Back-end:** O Back-end visa fornecer as funcionalidades essenciais para este projeto.
- **Setor 4 – Testers / Documentação:** A Documentação tem como objetivo fornecer um relatório detalhado e claro sobre cada etapa do projeto.


## Atualização de Desenvolvimento - 25/09/2024

### Setor 1 – Design:
- Planejamento de como ficará o projeto por meio do Figma.
- Escolha da paleta de cores.
- Início ao desenvolvimento da logo.
- Busca por ícones.

### Setor 2 - Front-end:
- Criação da base do projeto.
- Organização das pastas.

### Setor 3 – Back-end:
- Arquitetura de pastas.
- Criação de arquivos.
- Fluxograma.

### Setor 4 – Testers / Documentação:
- Introdução
- Explicação dos setores com seus respectivos integrantes.
- Prévia de cada setor (o que esperam do projeto de acordo com sua função).
- Atualização de Desenvolvimento (o que foi feito no projeto de acordo com a data).

# Atualização de Desenvolvimento - 26/09/2024

## Setor 1 – Design
- Planejamento do cadastro do projeto utilizando o Figma.

## Setor 2 – Front-end
- Início do desenvolvimento do código conforme o planejamento.
- Pesquisa de fontes.

## Setor 3 – Back-end
- Revisão do planejamento do projeto.
- Início da configuração do banco de dados.
- Criação de fluxograma.

## Setor 4 – Testers / Documentação
- Atualização de Desenvolvimento 26/09/2024.


# Atualização de Desenvolvimento - 28/09/2024

## Setor 2 – Front-end
- Códigos formatados.
- Imagens acrescentadas.
- Funções estáticas adicionadas.

# Atualização de Desenvolvimento - 29/09/2024

## Setor 3 – Back-end
- Corrigidos os caminhos para arquivos estáticos (CSS, JS, imagens) no login.html e index.html.
- Implementada rota para redirecionar ao index.html após login bem-sucedido.
- Adicionada nova rota '/index' para servir a página principal (index.html).

## Setor 4 – Testers / Documentação
- Atualização de Desenvolvimento 29/09/2024.


# Atualização de Desenvolvimento - 30/09/2024

## Setor 3 – Back-end

### Funcionalidades Adicionadas

1. **Login com Verificação de Credenciais**
   - Implementada funcionalidade de login com verificação de credenciais no banco de dados.
   - Utilização de `werkzeug.security` para hash e verificação de senha.
   - Rota de login verifica o hash da senha armazenada no banco de dados.

2. **Sessão de Usuário**
   - Implementada sessão de usuário para controle de acesso, diferenciando entre usuários comuns e administradores.
   - Sessão de usuário implementada para manter o estado de login.

3. **Página de Administração**
   - Criada página de administração que lista produtos, permitindo o cálculo automático de lucro unitário e total.
   - Página exclusiva para usuários com perfil de administrador (/admin).
   - Exibição de produtos cadastrados com cálculo de lucro unitário e total.

4. **Cadastro de Novos Produtos**
   - Adicionada rota para cadastro de novos produtos, permitindo que administradores insiram produtos diretamente no sistema.
   - Permite o cadastro de produtos com nome, preço de compra, preço de venda, e quantidade.
   - Dados são inseridos no banco de dados e exibidos na página de administração.

5. **Funcionalidade de Logout**
   - Implementada funcionalidade de logout, removendo as sessões ativas do usuário.
   - Remove informações da sessão do usuário e redireciona para a página de login.

6. **Melhorias nas Mensagens de Erro**
   - Melhorias nas mensagens de erro para feedback mais claro ao usuário, especialmente em credenciais inválidas e problemas de conexão ao banco.

7. **Produto aparecendo para o Usuario**
   - Agora quando um produto é adicionado pelo admin, ele é automaticamente exposta na pagina do usuario.

8. **Proteção de Rotas**

- Implementada verificação de sessão para proteger páginas restritas (admin e index).
- Usuário é redirecionado ao login se não estiver autenticado.

## Setor 4 – Testers / Documentação
- Atualização de Desenvolvimento 30/09/2024.

# Atualização de Desenvolvimento - 01/10/2024

## Setor 2 – Front-end
- Atualização da página inicial com a inserção de produtos.

## Setor 3 – Backend
- Implementada a tabela `carrinho` para gerenciar produtos desejados pelos usuários.
  - Colunas: `id`, `usuario_id`, `produto_id`, `quantidade`, `preco_venda`, `total_preco`, `imagem_url`.
  - `produto_id` como chave estrangeira referenciando a tabela `produtos`.

## Setor 4 – Testers / Documentação
- Atualização de Desenvolvimento 01/10/2024.






