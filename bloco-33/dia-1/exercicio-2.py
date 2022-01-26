class Retangulo:
    def __init__(self, lado_a, lado_b):
        self.lado_a = lado_a
        self.lado_b = lado_b

    def calcula_area(self):
        return self.lado_a * self.lado_b

    def calcula_perimetro(self):
        return (2 * self.lado_a) + (2 * self.lado_b)


leRetangulo = Retangulo(5, 10)


print(leRetangulo.lado_a)
print(leRetangulo.lado_b)
print(leRetangulo.calcula_area())
print(leRetangulo.calcula_perimetro())
