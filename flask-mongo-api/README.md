
# Before run the app

##Create virtualenv

virtualenv flask-mongo-api-env

##Create mongo db and insert data

$> use bookstore

$> db.bookdetails.insert({title: 'The shining', author: 'Stephen King'})

# Using API

Get all books
GET - localhost:5000/api/book/v1/books

Create a new books
POST - localhost:5000/api/book/v1/books
{
	"title": "The shining",
	"author": "Stephen King"
}


DELETE - localhost:5000/api/book/v1/books/<int:book_id>


PUT - localhost:5000/api/book/v1/books/<int:book_id>
{
	"title": "The shining - UPDATED",
	"author": "Stephen King"
}


GET - localhost:5000/api/book/v1/books/<int:book_id>
