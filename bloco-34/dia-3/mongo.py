from pymongo import MongoClient
import json

client = MongoClient()
db = client.library
with open("./books.json", "r") as file:
    document = json.load(file)

# print(document)
books = db.books.insert_many(document)
client.close()