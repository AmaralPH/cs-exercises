import json
import csv


def retrive_books(file):
    return [json.loads(line) for line in file]


def list_categories(books):
    categories_set = set()
    for book in books:
        if len(book["categories"]) > 0:
            categories_set.update(book["categories"])
    categories_set.discard("")
    return categories_set


def count_categories(books):
    categories_list = list_categories(books)
    categories_dict = {categorie: 0 for categorie in categories_list}
    for book in books:
        for categorie in book["categories"]:
            if categorie in categories_list:
                categories_dict[categorie] += 1
    return categories_dict


def books_with_categories(books):
    book_count = 0
    for book in books:
        if len(book["categories"]) > 0:
            book_count += 1
    return book_count


def categories_percentage(books):
    total_of_books = books_with_categories(books)
    print(total_of_books)
    categories_list = list_categories(books)
    print(categories_list)
    categories_dict = count_categories(books)
    print(categories_dict)
    for categorie in categories_list:
        categories_dict[categorie] = (
            categories_dict[categorie] / total_of_books
        )
    return categories_dict


if __name__ == "__main__":
    with open("./arquivos/books.json") as file:
        books = retrive_books(file)

    data = categories_percentage(books)

    with open("./arquivos/relatorio.csv", "w") as file:
        writer = csv.writer(file)

        headers = ["Categoria", "Porcentagem"]

        writer.writerow(headers)

        for categoria, porcentagem in data.items():
            row = [categoria, porcentagem]
            writer.writerow(row)
