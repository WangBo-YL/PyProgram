'''
Program: API
Author: Bo Wang
Last Updated: 2/10/2024
Description: This program is an API for a book store.
'''
from flask import Flask, request, jsonify
app = Flask(__name__)
from flask_sqlalchemy import SQLAlchemy

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_name = db.Column(db.String(80), unique=True, nullable=False)
    author = db.Column(db.String(80), nullable=False)
    publisher = db.Column(db.String(80))

    def __repr__(self):
        return f"Book('{self.book_name}', '{self.author}', '{self.publisher}')"
    
@app.route('/')
def index():
    return "Hello! This is the home page."

@app.route('/Books')
def get_books():
    try:
        books = Book.query.all()
        output = []
        for book in books:
            book_data = {'book_name': book.book_name, 'author': book.author, 'publisher': book.publisher}
            output.append(book_data)
        return {'books': output}
    except Exception as e:
        print(e)
        return {'Error': 'Something went wrong'}

@app.route('/Books/<id>')
def get_book(id):
    book = Book.query.get_or_404(id)
    return {'book_name': book.book_name, 'author': book.author, 'publisher': book.publisher}

@app.route('/Books', methods=['POST'])
def add_book():
    data = request.get_json()
    if not data or 'book_name' not in data or 'author' not in data or 'publisher' not in data:
        return jsonify({'error': 'Missing data'}), 400

    try:
        book = Book(book_name=data['book_name'], author=data['author'], publisher=data['publisher'])
        db.session.add(book)
        db.session.commit()
        return jsonify({'id': book.id, 'message': 'Book added successfully'}), 201
    except Exception as e:
        return jsonify({'error': 'Something went wrong', 'message': str(e)}), 500
    
@app.route('/Books/<id>', methods=['DELETE'])
def delete_book(id):
    book = Book.query.get_or_404(id)
    if book is None:
        return jsonify({'error': 'Book not found'}), 404
    try:
        db.session.delete(book)
        db.session.commit()
        return jsonify({'message': 'Book deleted successfully'}), 200
    except Exception as e:
        return jsonify({'error': 'Something went wrong', 'message': str(e)}), 500