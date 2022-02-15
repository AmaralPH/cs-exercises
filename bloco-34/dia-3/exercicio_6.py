from pymongo import MongoClient


def search_by_category():
    category = input("Informe a categoria: ")

    client = MongoClient()
    db = client.library
    books = db.books
    for book in books.find({ "categories": category }):
        print(book["title"])

    client.close()


if __name__ == "__main__":
    search_by_category()