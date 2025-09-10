# -*- coding: utf-8 -*-
# main.py

from inventory import PizzariaEstoque
from storage import StorageManager
from utils import limpar_tela, obter_inteiro

class CLI:
    """Interface de Linha de Comando para o sistema de estoque."""
    
    def __init__(self):
        storage_manager = StorageManager("estoque.json")
        self.pizzaria = PizzariaEstoque(storage_manager)
        self.opcoes = {
            "1": ("Cadastrar Produto", self.cadastrar_produto),
            "2": ("Adicionar ao Estoque", self.atualizar_estoque),
            "3": ("Consumir Produto", self.consumir_produto),
            "4": ("Relatório de Estoque", self.relatorio_estoque),
            "5": ("Sair", self.sair)
        }

    def exibir_menu(self):
        """Exibe o menu de opções para o usuário."""
        print("\n🍕 Sistema de Controle de Estoque da Pizzaria 🍕")
        print("===================================================")
        for chave, (descricao, _) in self.opcoes.items():
            print(f"{chave}. {descricao}")
        print("===================================================")
    
    def executar(self):
        """Loop principal da aplicação."""
        while True:
            self.exibir_menu()
            opcao = input("Digite a opção desejada: ")
            limpar_tela()

            acao = self.opcoes.get(opcao)
            if acao:
                acao[1]()  # Executa a função associada à opção
            else:
                print("❌ Opção inválida, tente novamente.")

    def cadastrar_produto(self):
        print("--- Cadastro de Novo Produto ---")
        try:
            nome = input("Nome do produto: ").strip()
            if not nome:
                print("❌ O nome do produto não pode ser vazio.")
                return
            quantidade = obter_inteiro(f"Quantidade inicial de '{nome}': ")
            limite_estoque = obter_inteiro(f"Limite de alerta para '{nome}': ")
            self.pizzaria.cadastrar_produto(nome, quantidade, limite_estoque)
        except ValueError as e:
            print(f"❌ Erro ao cadastrar: {e}")

    def atualizar_estoque(self):
        print("--- Adicionar ao Estoque ---")
        try:
            nome = input("Nome do produto: ").strip()
            quantidade = obter_inteiro(f"Quantidade para adicionar ao estoque de '{nome}': ")
            self.pizzaria.atualizar_estoque(nome, quantidade)
        except (KeyError, ValueError) as e:
            print(f"❌ Erro ao atualizar: {e}")

    def consumir_produto(self):
        print("--- Consumo de Produto ---")
        try:
            nome = input("Nome do produto consumido: ").strip()
            quantidade = obter_inteiro(f"Quantidade consumida de '{nome}': ")
            self.pizzaria.consumir_produto(nome, quantidade)
        except (KeyError, ValueError) as e:
            print(f"❌ Erro ao consumir: {e}")
            
    def relatorio_estoque(self):
        self.pizzaria.listar_produtos()
        input("Pressione Enter para continuar...")
        limpar_tela()

    def sair(self):
        """Encerra a aplicação."""
        print("Saindo do sistema. Até logo! 👋")
        exit()

if __name__ == "__main__":
    cli = CLI()
    cli.executar()