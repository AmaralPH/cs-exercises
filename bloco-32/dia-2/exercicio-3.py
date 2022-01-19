import random


with open("./arquivos/palavras.txt", "r") as file:
    words_list = []
    for line in file:
        words_list.append(line.replace("\n", ""))


def scramble_word(word):
    return "".join(random.sample(word, len(word)))


def word_game():
    word = random.choice(words_list)
    word_scrambled = scramble_word(word)
    for _ in range(3):
        print(f"Palavra embaralhada -> {word_scrambled}")
        bid = input("Escreva a palavra desembaralhada: ")
        if bid == word:
            print(f"Parabéns! Você acertou, a palavra era {word}")
            return
        print("Errou, tente de novo")
    print("Você não conseguiu, otário!")
    return


word_game()
