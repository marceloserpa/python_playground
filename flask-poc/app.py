from flask import Flask, request, jsonify, abort

app = Flask(__name__)
app.config.from_object(__name__)

books = []

@app.route('/api/book/v1/books',  methods=['GET'])
def get_books():
    return jsonify({"books": books})

@app.route('/api/book/v1/books',  methods=['POST'])
def create_book():
    book = {'id': len(books) + 1, 'title': request.json['title'], 'author': request.json['author']}
    books.append(book)
    return jsonify({"book": book}), 201

@app.route('/api/book/v1/books/<int:book_id>',  methods=['DELETE'])
def delete_book(book_id):
    for idx, val in enumerate(books):
        if val['id'] == book_id:
            del books[idx]
            return abort({'removed': True}), 404
    return jsonify({'removed': False}), 200

if __name__ == '__main__':
    app.run()

