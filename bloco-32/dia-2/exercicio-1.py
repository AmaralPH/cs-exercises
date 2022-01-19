def nome_vertical():
    nome = input("Insira um nome: ")
    for index in range(len(nome), 0, -1):
        print(nome)
        nome = nome[0:index - 1]


nome_vertical()
