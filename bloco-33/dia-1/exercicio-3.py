class Circulo:
    def __init__(self, raio):
        self.raio = raio
        self.PI = 3.14

    def calcula_area(self):
        return self.PI * self.raio ** 2

    def calcula_perimetro(self):
        return 2 * self.PI * self.raio


circulo = Circulo(5)


print(f"Raio do circulo = {circulo.raio}")
print(f"A area do circulo é = {circulo.calcula_area()}")
print(f"O perimetro do circulo é = {circulo.calcula_perimetro()}")
