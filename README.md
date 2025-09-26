🍕 Sistema de Controle de Estoque para Pizzaria
Um sistema de linha de comando (CLI) simples e eficiente para gerenciamento de estoque, desenvolvido em Python. Ele é projetado para ajudar pequenos negócios, como uma pizzaria, a controlar seus produtos de forma organizada, com persistência de dados e alertas de estoque baixo.


pizzaria_estoque/
├── main.py              # Ponto de entrada e interface com o usuário (CLI)
├── models.py            # Definição da classe de dados `Produto`
├── inventory.py         # Lógica de negócio para gerenciar o estoque
├── storage.py           # Lógica para salvar e carregar dados em JSON
├── utils.py             # Funções utilitárias (limpar tela, validação de input)
└── estoque.json         # Arquivo de banco de dados (gerado automaticamente)

Como Usar:
Ao executar main.py, um menu interativo será exibido no terminal:


Melhorias Futuras
Este projeto é um ótimo ponto de partida. Algumas ideias para evoluí-lo:

[ ] Implementar a funcionalidade de excluir ou editar um produto.

[ ] Adicionar testes unitários para garantir a robustez da lógica de negócio.

[ ] Criar relatórios mais avançados (ex: exportar para CSV).

[ ] Desenvolver uma interface mais rica com bibliotecas como rich ou curses.

[ ] Migrar a persistência de dados para um banco de dados como SQLite.

