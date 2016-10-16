from flask import Flask, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)
app.config.from_object(__name__)

mongo_client = MongoClient('localhost:27017')
db = mongo_client.bookstore

@app.route('/api/book/v1/books',  methods=['GET'])
def get_books():
    books = []
    books_find = db.bookdetails.find()
    for book in books_find:
        books.append({'id': book['id'], 'title': book['title'], 'author': book['author']})
    return jsonify({"books": books})

@app.route('/api/book/v1/books',  methods=['POST'])
def create_book():
    total_books = db.bookdetails.count()
    book = {"id": total_books + 1, "title": request.json['title'], "author": request.json['author']}
    print db.bookdetails.insert_one(book).inserted_id
    return jsonify({"message": "created"})

@app.route('/api/book/v1/books/<int:book_id>',  methods=['DELETE'])
def delete_book(book_id):
    try:
        db.bookdetails.delete_many({'id': {'$in': [book_id]}})
        return jsonify({'message': 'Deletion successful'}), 201
    except Exception, e:
        print str(e)
        return jsonify({'message': 'Deletion error'}), 400


@app.route('/api/book/v1/books/<int:book_id>',  methods=['GET'])
def find_book(book_id):
    books = []
    books_find = db.bookdetails.find({"id": book_id})
    for book in books_find:
        books.append({'id': book['id'], 'title': book['title'], 'author': book['author']})
    return jsonify({"books": books})


@app.route('/api/book/v1/books/<int:book_id>',  methods=['PUT'])
def update_book(book_id):
    db.bookdetails.update_one(
        {'id': {'$in': [book_id]}},
        {
            "$set": {
                "title": request.json['title'],
                "author": request.json['author']
            }
        }
    )
    return jsonify({'message': 'updated'}), 200


if __name__ == '__main__':
    app.run()

