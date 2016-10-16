
## Before run the app

$> use bookstore

$> db.bookdetails.insert({title: 'The shining', author: 'Stephen King'})


GET - localhost:5000/api/book/v1/books


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