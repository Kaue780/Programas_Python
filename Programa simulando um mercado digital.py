# Nome: Sistema de Supermercado
# Autor: Kauê Lima Marques
# Data: 27/11/2025
# Descrição: Programa simulando um mercado digital



def inicio():
    print("  BEM-VINDO AO MERCADO DIGITAL  ")
    print("1 - Cadastrar")
    print("2 - Login")
    opc = input("Escolha uma opção: ")

    if opc == "1":
        print("Você está sendo direcionado para a tela de cadastro")
        cadastro()
    elif opc == "2":
        print("Você está sendo direcionado para tela de login")
        login()
    else:
        print("Erro, tente novamente.")
        inicio()

def cadastro():
    nome = input("Digite seu nome de usuário: ")
    senha = input("Digite uma senha somente com números: ")
    if nome in nome_de_usuario: #se o nome do usuario está na lista
        if senha in senha_lista: # se a senha do usuario está na lista de senha
            print("Usuário já existe!")
            login()
    else:
        nome_de_usuario.append(nome)
        senha_lista.append(senha)
        print("O cadastro foi realizado com sucesso.")
        login()

def login():
    nome = input("Digite seu nome de usuário: ")
    senha = input("Digite uma senha somente com números: ")
    if nome in nome_de_usuario:
        if senha in senha_lista:
            if nome_de_usuario.index(nome) == senha_lista.index(senha):
                print("Seja bem vindo.")
                categorias()
            else:
                print("Usuário ou senha incorreta")
                b = int(input("1 - Tentar Novamente.\n2 - Realizar Cadastro."))
                if b == 1:
                    login()
                elif b == 2:
                    cadastro()
                else:
                    print("Opção não encontrada, retornando para tela inicial.")
                    inicio()
        else:
            print("Usuário ou senha incorreta")
            b = int(input("1 - Tentar Novamente.\n2 - Realizar Cadastro. "))
            if b == 1:
                login()
            elif b == 2:
                cadastro()
            else:
                print("Opção não encontrada, retornando para tela inicial.")
                inicio()
    else: # se o usuario n tiver o nome no banco de dados vai refazer a funçao login
        print("Usuário ou senha incorreta")
        b = int(input("1 - Tentar Novamente.\n2 - Realizar Cadastro. "))
        if b == 1:
            login()
        elif b == 2:
            cadastro()
        else:
            print("Opção não encontrada, retornando para tela inicial.")
            inicio()

def mostrar_categoria(produtos, precos):
    print("\nProdutos disponíveis:")
    for i in range(len(produtos)):
        print(f"{i+1} - {produtos[i]} ({precos[i]})")
    
    while True:
        escolha = input("Digite o número do produto para adicionar ao carrinho (ou 0 para voltar): ")
        if escolha == "0":
            break
        indice = int(escolha) - 1
        carrinho.append(precos[indice])
        print(f"{produtos[indice]} adicionado ao carrinho.")


def categorias():
    print("Aqui estão as categorias do nosso supermercado abrindo a categoria, você terá acesso a todos os nossos itens.")
    print("1 - Mercearia")
    print("2 - Limpeza")
    print("3 - Frutas")
    print("4 - Frios")
    print("5 - Bebidas")
    print("6 - Congelados")
    print("7 - Padaria")
    print("8 - Finalizar compra")
    print("9 - Retirar produto")
    print("10 - Pesquisar item")
    print("11 - Sair")
    opc = input("Escolha uma opção: ")

    if opc == "1":
        mostrar_categoria(mercearia, mercearia_preços)
        categorias()

    elif opc == "2":
        mostrar_categoria(limpeza, limpeza_preços)
        categorias()

    elif opc == "3":
        mostrar_categoria(frutas, frutas_preços)
        categorias()

    elif opc == "4":
        mostrar_categoria(frios, frios_preços)
        categorias()

    elif opc == "5":
        mostrar_categoria(bebidas, bebidas_preços)
        categorias()

    elif opc == "6":
        mostrar_categoria(congelados, congelados_preços)
        categorias()

    elif opc == "7":
        mostrar_categoria(padaria, padaria_preços)
        categorias()

    elif opc == "8":
        # Soma o carrinho
        total = 0
        for preco in carrinho:
            total += float(preco.replace("R$", "").replace(",", "."))
        print("\nTotal da compra: R$", round(total, 2))
        print("Deseja finalizar a compra?")
        escolha = input("Digite 1 para Sim ou digite 2 para Não: ")
        if escolha == "1":
            print("Obrigado por comprar no nosso supermercado!")
            categorias()

        elif escolha == "2":
            print("Estamos retornando para a tela de compras...")
            categorias()

        else:
            print("ERRO, opção não encontrada voltando para a tela de compras...")
            categorias()

    elif opc == "9":
        print(carrinho)
        print("Escolha qual produto deseja tirar, informe o número dele na lista")
        print("Lembrando se você quiser tirar o 2 item do seu carrinho você deve diminuir 1 número, Ex: tenho arroz e café e quero tirar o café eu coloco o número 1")
        vlr = int(input("Coloque o número que ele está na lista da esquerda para a direita: "))
        carrinho.pop(vlr)
        print(carrinho)
        categorias()

    elif opc == "10":
        pesq()

    elif opc == "11":
        print("Saindo...")
        inicio()

    else:
        print("Opção não encontrada!")
        categorias()

def pesq():
    prod = input("Digite o nome do produto que deseja procurar: ")
    if prod in mercearia:
        print("Produto pertece a categoria de Mercearia")
        categorias()
    elif prod in limpeza:
        print("Produto pertence a categoria de Limpeza")
        categorias()
    elif prod in frutas:
        print("Produto pertence a categoria de Frutas")
        categorias()
    elif prod in frios:
        print("Produto pertence a categoria de Frios")
        categorias()
    elif prod in bebidas:
        print("Produto pertence a categoria de Bebidas")
        categorias()
    elif prod in congelados:
        print("Produto pertence a categoria de Congelados")
        categorias()
    elif prod in padaria:
        print("Produto pertence a categoria de Padaria")
        categorias()
    else:
        print("Produto não existe na loja")
        categorias()

mercearia = ["Arroz", "Feijão", "Açúcar", "Açúcar Refinado", "Café", "Chá", "Achocolatado", "Leite", "Fermento", "Macarrão", "Molho de Tomate", "Extrato de Tomate", "Leite Condensado", "Creme de Leite", "Azeite", "Vinagre", "Sal"]
limpeza = ["Detergente Líquido", "Desinfetante", "Água Sanitária", "Sabão em pó", "Amaciante", "Álcool", "Papel Toalha", "Guardanapo", "Papel Higiênico", "Shampoo", "Condicionador", "Sabonete", "Desodorante", "Creme Dental", "Escova de Dente"]
frutas = ["Alface", "Repolho", "Vagem", "Tomate", "Pepino", "Cebola", "Batata Doce", "Batata", "Cenoura", "Chuchu", "Limão", "Banana"]
frios = ["Leite", "Mateiga", "Iorgute", "Requeijão", "Queijo", "Queijo Muçarela", "Presunto"]
bebidas = ["Água Mineral", "Refrigerante", "Suco", "Cerveja", "Vinho"]
congelados = ["Bife", "Carne Moída", "Carne de Frango", "Carne de Porco", "Presunto (Fatiado)", "Muçarela", "Salsicha", "Linguiça"]
padaria = ["Bolo", "Torta", "Torta Doce", "Salgadinho", "Pão", "Pão Doce", "Bolacha (ou biscoito)", "Salgados", "Sanduíche"]
mercearia_preços = ["R$ 7,00", "R$ 9,00", "R$ 5,00", "R$ 5,50", "R$ 18,00", "R$ 8,00", "R$ 12,00", "R$ 6,00", "R$ 2,00", "R$ 4,00", "4,50", "R$ 5,00", "R$ 7,00", "R$ 4,50", "R$ 25,00", "R$ 4,50", "R$ 3,00"]
limpeza_preços = ["R$ 5,00", "R$ 6,00", "R$ 7,00", "R$ 12,00", "R$ 10,00", "R$ 6,00", "R$ 8,00", "R$ 5,00", "R$ 10,00", "R$ 15,00", "R$ 15,00", "R$ 4,00", "R$ 12,00", "R$ 8,00", "R$ 7,00"]
frutas_preços = ["R$ 4,00", "R$ 8,00", "R$ 10,00", "R$ 10,00", "R$ 3,50", "R$ 7,00", "R$ 6,00", "R$ 5,50", "R$ 6,00", "R$ 5,00", "R$ 7,00", "R$ 10,00"]
frios_preços = ["R$ 6,00", "R$ 12,00", "R$ 5,00", "R$ 7,00", "R$ 8,00", "R$ 9,00", "R$ 6,00"]
bebidas_preços = ["R$ 2,50", "R$ 10,00", "R$ 8,00", "R$ 5,00", "R$ 40,00"]
congelados_preços = ["R$ 45,00", "R$ 30,00", "R$ 20,00", "R$ 25,00", "R$ 10,00", "R$ 18,00", "R$ 20,00", "R$ 22,00"]
padaria_preços = ["R$ 20,00", "R$ 25,00", "R$ 25,00", "R$ 8,00", "R$ 12,00", "R$ 3,50", "R$ 6,00", "R$ 4,00", "R$ 15,00"]

nome_de_usuario = []
senha_lista = []
carrinho = []
inicio()