with open("./arquivos/palavras.txt", "r") as file:
    content = file.read().split(", ")


with open("./arquivos/palavras.txt", "w") as file:
    newContent = ""
    for word in content:
        newContent += f"{word.replace(' ', '')}"
    file.write(newContent)