# Nome: Sistema de Banco
# Autor: Kauê Lima Marques
# Data: 11/11/2025
# Descrição: Programa simulando um caixa eletrônico de bancos



def tela_inicial():
    print("  BEM-VINDO AO BANCO PYTHON  ")
    print("1️⃣ Criar Nova Conta")
    print("2️⃣  Fazer Login")
    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        print("Você está sendo direcionado para tela de cadastro")
        cadastrar()
    elif escolha == "2":
        print("Você está sendo direcionado para a tela de login")
        login()
    else:
        print("Opção não encontrada! Tente novamente.")
        tela_inicial()

def cadastrar():
    print("\n=== CADASTRO ===") 
    usuario = input("Digite um nome de usuário: ")
    senha = input("Digite uma senha, somente com números: ")
    if usuario in usuarios: #se o nome do usuario está na lista
        if senha in senhas: # se a senha do usuario está na lista de senha
            print("Usuário já existe!")
            login()
    else:
        usuarios.append(usuario) # append vai adiciona o nome de usuario na lista
        senhas.append(senha)
        saldos.append(300)
        print("O cadastro foi realizado com sucesso.")
        print("Você recebeu R$300,00 reais.")
        print(usuarios) # teste para ver se funcionou (n é importante) / e o cadastro está feito nenhum erro
        print(senhas)
        print(saldos)
        login()

def login(): #Lembrete 
    print("\n=== LOGIN ===")
    usuario = input("Digite seu nome de usuário: ")
    senha = input("Digite sua senha: ")
    if usuario in usuarios: #se o nome do usuario está na lista
        if senha in senhas: # se a senha do usuario está na lista de senha
            if usuarios.index(usuario) == senhas.index(senha):
                print("Seja bem vindo.")
                conta(senha)
            else:
                print("Usuário ou senha incorreta")
                b = int(input("1 - Tentar Novamente.\n2 - Realizar Cadastro."))
                if b == 1:
                    login()
                elif b == 2:
                    cadastrar()
                else:
                    print("Opção não encontrada, retornando para tela inicial.")
                    tela_inicial()
        else:
            print("Usuário ou senha incorreta")
            b = int(input("1 - Tentar Novamente.\n2 - Realizar Cadastro. "))
            if b == 1:
                login()
            elif b == 2:
                cadastrar()
            else:
                print("Opção não encontrada, retornando para tela inicial.")
                tela_inicial()
    else: # se o usuario n tiver o nome no banco de dados vai refazer a funçao login
        print("Usuário ou senha incorreta")
        b = int(input("1 - Tentar Novamente.\n2W - Realizar Cadastro. "))
        if b == 1:
            login()
        elif b == 2:
            cadastrar()
        else:
            print("Opção não encontrada, retornando para tela inicial.")
            tela_inicial()
    
def conta(senha):
    print("1 Consultar Saldo")
    print("2 Realizar Saque")
    print("3 Realizar Depósito")
    print("4 Sair")
    selecione = input("Escolha uma opção: ")

    if selecione == "1":
        print("Você está sendo direcionado para tela de Saldo\n")
        saldo(senha)
    elif selecione == "2":
        print("Você está sendo direcionado para a tela de Saque\n")
        saque(senha)
    elif selecione == "3":
        print("Você está sendo redirecionado para a tela de Depósito\n")
        dep(senha)
    else:
        print("Opção não encontrada! Tente novamente.\n")
        tela_inicial()

def saldo(senha):
    a = saldos[senhas.index(senha)]
    print(f"O seu saldo agora é de {a} reais\n")
    conta(senha)

def saque(senha):
    a = saldos[senhas.index(senha)]
    b = float(input("Digite o valor que deseja sacar: "))
    if b>a:
        print("Transação inválida, o valor da conta é menor que o valor de saque.")
        conta(senha)
    else:
        saldos[senhas.index(senha)] = saldos[senhas.index(senha)] - b
        conta(senha)

def dep(senha):
    a = saldos[senhas.index(senha)]
    b = float(input("Digite o valor que deseja depositar: "))
    saldos[senhas.index(senha)] = saldos[senhas.index(senha)] + b
    conta(senha)

usuarios = []  #lista d pessoas que n são cadastradas
senhas = [] #lista de senhas que vão ser cadastradas
saldos = [] #lista de saldo que o usuário tem no banco
tela_inicial()