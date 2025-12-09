# Nome: Sistema de Contas matemáticas
# Autor: Kauê Lima Marques
# Data: 13/11/2025
# Descrição: Programa simulando uma calculadora, fazendo diversos calculos



def tela_ini():
    print("  BEM-VINDO A CALCULADORA DIGITAL  ")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Divisão")
    print("4 - Multiplicação")
    print("5 - Potência")
    escolha = input("Escolha uma opção: ")

    try:    # O try em Python tenta executar um código que pode gerar erro. Se ocorrer um erro, o except captura e trata, evitando que o programa quebre. Isso deixa o programa mais seguro e amigável ao usuário.
        num = float(input("Coloque o primeiro número: "))
        num2 = float(input("Coloque o segundo número: "))
    except ValueError:  # o except captura e trata, evitando que o programa quebre. Isso deixa o programa mais seguro e amigável ao usuário.
        print("Erro: você não digitou um número inteiro válido.")
        tela_ini()

    if escolha == "1":
        print("Você está sendo direcionado para a área de soma.\n")
        soma(num, num2)

    elif escolha == "2":
        print("Você está sendo direcionado para a área de subtração.\n")
        sub(num,num2)
        
    elif escolha == "3":
        print("Você está sendo direcionado para a área de divisão.\n")
        div(num,num2)

    elif escolha == "4":
        print("Você está sendo direcionado para a área de multiplicação.\n")
        mult(num,num2)

    elif escolha == "5":
        print("Você está sendo direcionado para a área de potênciação.\n")
        pot(num,num2)

    else:
        print("Erro, tente novamente.\n")
        tela_ini()

def soma(num, num2):

    result = num + num2
    print(f"O resultado da sua conta de soma é: {result:.4f}\n")    # {result:.4f} usei para colocar virgula após o numero inteiro
    escolha()

def sub(num, num2):
    result = num - num2
    print(f"O resultado da sua conta de subtração é: {result:.4f}\n")
    escolha()

def div(num, num2):
    result = num / num2
    print(f"O resultado da sua conta de divisão é: {result:.4f}\n")
    escolha()

def mult(num, num2):
    result = num * num2
    print(f"O resultado da sua conta de multiplicação é: {result:.4f}\n")
    escolha()

def pot(num, num2):
    result = num ** num2
    print(f"O resultado da sua conta de potencia é: {result:.4f}\n")
    escolha()

def escolha():
    esc = input("Deseja continuar fazendo calculos? Sim ou Não\n")
    if esc == "Sim":
        tela_ini()
    elif esc == "Não":
        print("Saindo...")
    else:
        print("Erro, tente novamente.")
        tela_ini()

tela_ini()