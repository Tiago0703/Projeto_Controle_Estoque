# -*- coding: utf-8 -*-
# utils.py

import os
import platform

def limpar_tela():
    """Limpa o terminal, compatível com Windows, Linux e Mac."""
    sistema = platform.system()
    if sistema == "Windows":
        os.system('cls')
    else:
        os.system('clear')

def obter_inteiro(prompt: str) -> int:
    """Solicita um número inteiro ao usuário e lida com entradas inválidas."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("❌ Erro: Por favor, insira um número inteiro válido.")