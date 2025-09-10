# -*- coding: utf-8 -*-
# storage.py

import json
from typing import Dict
from models import Produto

class StorageManager:
    """
    Gerencia a persistência de dados do estoque em um arquivo JSON.
    """
    def __init__(self, filepath: str = "estoque.json"):
        self.filepath = filepath

    def carregar_estoque(self) -> Dict[str, Produto]:
        """
        Carrega o estoque de um arquivo JSON.
        Retorna um dicionário vazio se o arquivo não existir.
        """
        try:
            with open(self.filepath, 'r', encoding='utf-8') as f:
                dados_brutos = json.load(f)
                return {nome: Produto.from_dict(dados) for nome, dados in dados_brutos.items()}
        except (FileNotFoundError, json.JSONDecodeError):
            return {}

    def salvar_estoque(self, estoque: Dict[str, Produto]):
        """
        Salva o estado atual do estoque em um arquivo JSON.
        """
        with open(self.filepath, 'w', encoding='utf-8') as f:
            dados_serializados = {nome: produto.to_dict() for nome, produto in estoque.items()}
            json.dump(dados_serializados, f, indent=4, ensure_ascii=False)