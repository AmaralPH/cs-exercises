def eh_triangulo(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        if a == b == c:
            print("Triângulo Equilátero: três lados iguais")
        elif a == b or a == c or c == b:
            print("Triângulo Isósceles: quaisquer dois lados iguais")
        else:
            print("Triângulo Escaleno: três lados diferentes.")
    else:
        print("Não é triangulo")

if __name__ == "__main__":
    eh_triangulo(3, 4, 5)
    eh_triangulo(5, 5, 5)
    eh_triangulo(4, 4, 5)
    eh_triangulo(3, 4, 20)
