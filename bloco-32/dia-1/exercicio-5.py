import math

METROS_LITRO = 3
LITROS_LATA = 18
PRECO_LATA = 80

def custo_parede(metragem):
    litros = metragem / METROS_LITRO
    latas = math.ceil(litros / LITROS_LATA)
    return latas * PRECO_LATA

if __name__ == '__main__':
    print(custo_parede(1))
    print(custo_parede(3 * 18 + 1))


