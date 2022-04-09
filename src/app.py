from flask import Flask, abort, request, jsonify

app = Flask(__name__)


books = [
    {"id": 1, "title": "The subtle art of not giving a fuck", "author": "Mark Manson"},
    {"id": 2, "title": "Cracking Coding Interview", "author": "Dayle Laakmann McDowell"},
    {"id": 3, "title": "How not to die", "author": "Michael Greger" },
    {"id": 4, "title": "Meditation and Mindfulness", "author": "Andy Puddicombe"},
    {"id": 5, "title": "The Monk Who Sold His Ferrari", "author": "Robin Sharma"}
]

@app.route('/', methods=["GET"])
def index():
    return { "id": 1, "message": "Welcome to hands-on DevOps Workshop"}

@app.route("/api/v1/books", methods=["GET"])
def get_books():
    return { "books": books }

@app.route("/api/v1/books/<int:id>", methods=["GET"])
def get_book(id: int):
    for book in books:
        if book["id"] == id:
            return book
    return abort(404) 
    

# @app.route("/api/v1/books/", methods=["POST"])
# def add_book():
#     book = dict(request.get_json(force=True))
#     book["id"] = len(books) + 1
#     books.append(book)
#     return book

@app.route("/api/v1/books/<int:id>", methods=["DELETE"])
def delete_book(id: int):
    for index, book in enumerate(books):
        if book["id"] == id:
            del books[index]
            return book
    return abort(404)


if __name__ == '__main__':
    app.run()