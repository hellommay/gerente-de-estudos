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

def registrar_sessao():
    print("\n --- REGISTRAR NOVA VERSÃO ---")

    fase = ler_inteiro("Digite o numero da fase estudada: ")
    minutos = ler_inteiro("Digite o tempo de estudo (em minutos): ")
    nota = ler_inteiro("Dê uma nota de 1 a 5 para a sessão: ")

    while nota < 1 or nota > 5:
        print("ERROR: A nova deve ser de 1 à 5.")
        nota = ler_inteiro("Dê uma nota de 1 a 5 para a sessão: ")

    data_atual = datetime.now().strftime("%d-%m-%Y %H:%M")

    with open(ARQUIVO_DADOS, "a", encoding="utf-8") as arquivo:
        arquivo.write(f"{data_atual};{fase};{minutos};{nota}\n")

    print("Sessão registrada com sucesso!")
