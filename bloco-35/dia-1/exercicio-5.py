from math import random


def create_random_array(n):
    list_of_averages = []
    for _ in range(100):
        average = 0
        for _ in range(n):
            average += random.randrange(1, n)
        average = average/n
        list_of_averages.append(average)

    return list_of_averages


# tempo = O(n*n/10 + n*10)
# espaço = O(n)