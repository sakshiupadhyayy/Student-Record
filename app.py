from flask import Flask,request, jsonify
from pymongo import MongoClient
from bson import ObjectId
import json

app = Flask(__name__)

client = MongoClient('mongodb://localhost:27017/')
db = client['library']
books_collection = db['books']

@app.route('/books', methods=['GET'])
def get_all_books():
    books = books_collection.find()
    books = [{'_id': str(book['_id']), 'title': book['title'], 'author': book['author']} for book in books]
    return jsonify({'result': books})

@app.route('/books', methods=['POST'])
def add_book():
    book = request.json
    result = None
    try:
        db.books.insert_one(book)
        result = {'result': 'Book added successfully!'}
    except Exception as e:
        result = {'error': str(e)}
    return jsonify({'result': 'Book added successfully!', 'id': str(result.inserted_id)}), 201, {'Content-Type': 'application/json', 'Access-Control-Allow-Origin': '*'}

if __name__ == '__main__':
    app.run(debug=True)


