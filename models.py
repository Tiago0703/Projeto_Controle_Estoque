# -*- coding: utf-8 -*-
# models.py

from dataclasses import dataclass, field
from typing import Dict

@dataclass
class Produto:
    """
    Representa um produto no estoque da pizzaria.
    Utiliza dataclass para um código mais limpo e conciso.
    """
    nome: str
    quantidade: int = 0
    limite_estoque: int = 10
    
    def __post_init__(self):
        """Validação dos dados após a inicialização."""
        if self.quantidade < 0:
            raise ValueError("A quantidade não pode ser negativa.")
        if self.limite_estoque < 0:
            raise ValueError("O limite de estoque não pode ser negativo.")

    def esta_abaixo_do_limite(self) -> bool:
        """Verifica se a quantidade atual está abaixo ou igual ao limite de alerta."""
        return self.quantidade <= self.limite_estoque

    def to_dict(self) -> Dict:
        """Converte a instância do produto para um dicionário."""
        return {
            "nome": self.nome,
            "quantidade": self.quantidade,
            "limite_estoque": self.limite_estoque
        }

    @staticmethod
    def from_dict(data: Dict) -> 'Produto':
        """Cria uma instância de Produto a partir de um dicionário."""
        return Produto(
            nome=data["nome"],
            quantidade=data["quantidade"],
            limite_estoque=data["limite_estoque"]
        )