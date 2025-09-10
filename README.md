🍕 Sistema de Controle de Estoque para Pizzaria
Um sistema de linha de comando (CLI) simples e eficiente para gerenciamento de estoque, desenvolvido em Python. Ele é projetado para ajudar pequenos negócios, como uma pizzaria, a controlar seus produtos de forma organizada, com persistência de dados e alertas de estoque baixo.

✨ Funcionalidades
Cadastro de Produtos: Adicione novos produtos ao estoque com quantidade inicial e um limite para alertas.

Atualização de Estoque: Registre a entrada de novos itens para um produto já existente.

Registro de Consumo: Dê baixa em produtos que foram utilizados.

Relatórios: Visualize um relatório completo de todos os produtos, com suas quantidades, limites e status.

Persistência de Dados: O estoque é salvo em um arquivo estoque.json, garantindo que os dados não sejam perdidos ao fechar o sistema.

Alertas de Estoque Baixo: O sistema avisa automaticamente quando a quantidade de um produto atinge ou fica abaixo do limite pré-definido.

🏛️ Estrutura do Projeto
O projeto foi organizado com base no princípio da Separação de Responsabilidades (SoC), visando um código mais limpo, manutenível e escalável.

pizzaria_estoque/
├── main.py              # Ponto de entrada e interface com o usuário (CLI)
├── models.py            # Definição da classe de dados `Produto`
├── inventory.py         # Lógica de negócio para gerenciar o estoque
├── storage.py           # Lógica para salvar e carregar dados em JSON
├── utils.py             # Funções utilitárias (limpar tela, validação de input)
└── estoque.json         # Arquivo de banco de dados (gerado automaticamente)
main.py: Responsável por interagir com o usuário, exibir menus e capturar inputs.

inventory.py: Contém a classe PizzariaEstoque com toda a lógica para manipular os produtos, sem se preocupar com a interface ou o armazenamento.

models.py: Define a estrutura de um Produto usando dataclasses.

storage.py: Abstrai a lógica de leitura e escrita do arquivo estoque.json, permitindo que o sistema de armazenamento possa ser trocado facilmente no futuro (ex: para um banco de dados SQL).

🚀 Como Executar
Para executar este projeto, você precisará ter o Python 3 instalado em sua máquina.

Clone o repositório:

Bash

git clone https://github.com/SEU-USUARIO/pizzaria-estoque.git
(Substitua SEU-USUARIO/pizzaria-estoque pelo URL do seu repositório)

Navegue até o diretório do projeto:

Bash

cd pizzaria-estoque
Execute a aplicação:

Bash

python main.py
📋 Como Usar
Ao executar main.py, um menu interativo será exibido no terminal:

🍕 Sistema de Controle de Estoque da Pizzaria 🍕
===================================================
1. Cadastrar Produto
2. Adicionar ao Estoque
3. Consumir Produto
4. Relatório de Estoque
5. Sair
===================================================
Digite a opção desejada:
Basta digitar o número da opção desejada e pressionar Enter.

O sistema guiará você para inserir as informações necessárias para cada operação.

Ao sair, o estado atual do estoque estará salvo no arquivo estoque.json.

🛠️ Tecnologias Utilizadas
Python 3

Módulos Nativos: json, os, platform, dataclasses

Nenhuma dependência externa é necessária para rodar este projeto.

💡 Melhorias Futuras
Este projeto é um ótimo ponto de partida. Algumas ideias para evoluí-lo:

[ ] Implementar a funcionalidade de excluir ou editar um produto.

[ ] Adicionar testes unitários para garantir a robustez da lógica de negócio.

[ ] Criar relatórios mais avançados (ex: exportar para CSV).

[ ] Desenvolver uma interface mais rica com bibliotecas como rich ou curses.

[ ] Migrar a persistência de dados para um banco de dados como SQLite.

