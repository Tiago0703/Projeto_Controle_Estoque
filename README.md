📦 Projeto Controle de Estoque
Sistema simples de controle de estoque desenvolvido com foco educacional, com funcionalidades básicas para cadastrar, editar e remover produtos.

🧾 Descrição
Este projeto é uma aplicação de controle de estoque construída com Python, utilizando a biblioteca tkinter para interface gráfica e sqlite3 como banco de dados local. O objetivo é oferecer uma solução desktop leve e funcional para gerenciamento de produtos em estoque.

🛠️ Funcionalidades
📋 Cadastro de novos produtos com nome, categoria, valor e quantidade

🔍 Visualização em tabela dos produtos cadastrados

✏️ Edição dos dados de um produto existente

❌ Remoção de produtos do estoque

🗃️ Banco de dados local SQLite para persistência dos dados

🎨 Interface gráfica com tkinter (sem dependência de frameworks externos)

🖼️ Interface
A interface do sistema é baseada em tkinter, com uma janela principal que lista os produtos e botões para as ações básicas. A usabilidade é simples e intuitiva.

📂 Estrutura de Pastas
plaintext
Copiar
Editar
Projeto_Controle_Estoque/
│
├── main.py                 # Arquivo principal com a execução da interface
├── database.py             # Lida com criação e interação com o banco SQLite
├── interface.py            # Interface gráfica usando tkinter
├── estoque.db              # Banco de dados SQLite gerado automaticamente
├── README.md               # (Este arquivo)
└── requirements.txt        # Dependências do projeto (opcional)
▶️ Como executar
Pré-requisitos:
Python 3.x instalado no sistema

Instalação e execução:
bash
Copiar
Editar
git clone https://github.com/seuusuario/Projeto_Controle_Estoque.git
cd Projeto_Controle_Estoque
python main.py
Obs: O banco de dados estoque.db será criado automaticamente na primeira execução, se não existir.

🧩 Tecnologias utilizadas
Python 3

Tkinter

SQLite3

🤝 Contribuições
Contribuições são bem-vindas! Sinta-se à vontade para abrir issues, forks ou pull requests para sugerir melhorias ou correções.

👨‍💻 Autor
Desenvolvido por [Tiago Geisel de Oliveira]
📧 Email: [tiagogeisel4@gmail.com]

