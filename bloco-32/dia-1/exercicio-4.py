def maior_palavra(list):
    maior = ""
    for palavra in list:
        if len(palavra) > len(maior):
            maior = palavra
    return maior


if __name__ == "__main__":
    print(maior_palavra(["José", "Lucas", "Nádia", "Fernanda", "Cairo", "Joana"]))

