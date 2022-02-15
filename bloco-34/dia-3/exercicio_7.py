from pymongo import MongoClient


client = MongoClient()
db = client.library
books = db.books


query = [
    { "$match": { "status": "PUBLISH" } },
    { "$unwind": "$categories" },
    { "$group": { "_id": "$categories", "total": { "$sum": 1  } } },  
    { "$sort": { "total": -1, "_id": 1 } } 
  ]


list_of_books = list(books.aggregate(query))


for book in list_of_books:
    print(f"{book['_id']} {book['total']}")