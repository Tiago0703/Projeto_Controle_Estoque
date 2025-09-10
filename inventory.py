# -*- coding: utf-8 -*-
# inventory.py

from typing import Dict, Optional
from models import Produto
from storage import StorageManager

class PizzariaEstoque:
    """
    Classe principal para gerenciar as operações de estoque da pizzaria.
    """
    def __init__(self, storage_manager: StorageManager):
        self.storage = storage_manager
        self.estoque: Dict[str, Produto] = self.storage.carregar_estoque()

    def cadastrar_produto(self, nome: str, quantidade: int, limite_estoque: int):
        """Cadastra um novo produto no estoque."""
        if nome in self.estoque:
            raise ValueError(f"Produto '{nome}' já cadastrado!")
        
        produto = Produto(nome, quantidade, limite_estoque)
        self.estoque[nome] = produto
        self.storage.salvar_estoque(self.estoque)
        print(f"✅ Produto '{nome}' cadastrado com sucesso!")

    def atualizar_estoque(self, nome: str, quantidade_adicional: int):
        """Adiciona uma quantidade a um produto existente."""
        produto = self._get_produto(nome)
        if quantidade_adicional < 0:
            raise ValueError("Use a função de consumo para remover itens do estoque.")
            
        produto.quantidade += quantidade_adicional
        self.storage.salvar_estoque(self.estoque)
        print(f"🔄 Estoque de '{nome}' atualizado: {produto.quantidade} unidades.")

    def consumir_produto(self, nome: str, quantidade_consumida: int):
        """Consome uma quantidade de um produto do estoque."""
        produto = self._get_produto(nome)
        if quantidade_consumida < 0:
            raise ValueError("A quantidade a ser consumida não pode ser negativa.")
        if produto.quantidade < quantidade_consumida:
            raise ValueError(f"Quantidade insuficiente de '{nome}'. Em estoque: {produto.quantidade}.")

        produto.quantidade -= quantidade_consumida
        self.storage.salvar_estoque(self.estoque)
        print(f"🔻 Consumido {quantidade_consumida} de '{nome}'. Restante: {produto.quantidade} unidades.")

        if produto.esta_abaixo_do_limite():
            print(f"⚠️ Atenção: '{nome}' atingiu o limite de estoque ({produto.limite_estoque})!")

    def listar_produtos(self):
        """Retorna uma lista de todos os produtos no estoque."""
        if not self.estoque:
            print("ℹ️  Nenhum produto cadastrado no estoque.")
            return

        print("\n--- Relatório de Estoque ---")
        for produto in self.estoque.values():
            status = "⚠️  ABAIXO DO LIMITE" if produto.esta_abaixo_do_limite() else "✔ OK"
            print(f"- {produto.nome}: {produto.quantidade} unidades (Limite: {produto.limite_estoque}) - Status: {status}")
        print("--------------------------\n")

    def _get_produto(self, nome: str) -> Optional[Produto]:
        """Método auxiliar para buscar um produto e lançar erro se não encontrado."""
        produto = self.estoque.get(nome)
        if not produto:
            raise KeyError(f"Produto '{nome}' não encontrado no estoque!")
        return produto