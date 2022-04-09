from app import app, books

client = app.test_client()

def test_index():
    res = client.get('/')
    assert res.status_code == 200


def test_get_books():
    res = client.get('/api/v1/books')
    data = res.json
    assert res.status_code == 200
    assert len(data['books']) == len(books)


def test_get_book_return_200_Ok():
    res = client.get("/api/v1/books/1")
    data = res.json
    assert res.status_code == 200
    assert data['author'] == "Mark Manson"


def test_get_book_return_404():
    res = client.get("/api/v1/books/1000")
    assert res.status_code == 404

# def test_add_book():
#     count = len(books)
#     book = { "title": "Computer Science Unleashed", "author": "Wlaston Ferreira" }
#     res = client.post("/api/v1/books", json=book)
#     assert count < len(books)

def test_delete_return_200_ok():
    count = len(books)
    res = client.delete("/api/v1/books/1")

    assert res.json["id"] == 1
    assert len(books) < count

def test_delete_return_404():
    res = client.delete("/api/v1/books/100000")
    assert res.status_code == 404



