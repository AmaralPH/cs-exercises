def preco_total(litros, tipo):
    if litros <= 20:
        if tipo == "A":
            return litros * 1.9 * 0.97
        if tipo == "G":
            return litros * 2.5 * 0.95
    if litros > 20:
        if tipo == "A":
            return litros * 1.9 * 0.95
        if tipo == "G":
            return litros * 2.5 * 0.94


if __name__ == "__main__":
    print(preco_total(20, "A"))
    print(preco_total(30, "A"))
    print(preco_total(20, "G"))
    print(preco_total(30, "G"))