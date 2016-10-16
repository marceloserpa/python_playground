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
            return jsonify({'removed': True}), 200
    return jsonify({'error': 'not found'}), 404

@app.route('/api/book/v1/books/<int:book_id>',  methods=['GET'])
def find_book(book_id):
    for idx, val in enumerate(books):
        if val['id'] == book_id:
            return jsonify({'book': val}), 200
    return jsonify({'error': 'not found'}), 404

@app.route('/api/book/v1/books/<int:book_id>',  methods=['PUT'])
def update_book(book_id):
    for idx, val in enumerate(books):
        if val['id'] == book_id:
            books[idx]['title'] = request.json['title']
            books[idx]['author'] = request.json['author']
            return jsonify({'book': books[idx]}), 200
    return jsonify({'error': 'not found'}), 404


if __name__ == '__main__':
    app.run()

