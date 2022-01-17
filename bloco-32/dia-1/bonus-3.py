def somatorio(n):
    soma = 0;
    for i in range(1, n+1):
      soma += i
    return soma

if __name__ == '__main__':
    print(somatorio(5))
    print(somatorio(10))
    print(somatorio(3))