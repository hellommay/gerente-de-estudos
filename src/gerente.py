from datetime import datetime
import os

ARQUIVO_DADOS = "sessoes.txt"

def ler_inteiro(mensagem):
    while True:
        try:
            valor = int(input(memnsagem))
            return valor
        except ValueError:
            print("ERROR: Deve digitar um valor inteiro válido.")

