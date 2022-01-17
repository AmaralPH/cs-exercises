def media(list):
    soma = 0
    for num in list:
        soma += num
    media = soma / len(list)

    return media

if __name__ == '__main__':
    print(media([1, 2, 3, 4, 5, 6]))
