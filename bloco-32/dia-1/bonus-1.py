def menor(list):
    list.sort()
    return list[0]


if __name__ == '__main__':
    print(menor([5, 9, 3, 19, 70, 8, 100, 2, 35, 27]))
    print(menor([1, 10, 3, 0]))

