from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return { "id": 1, "message": "Welcome to hands-on DevOps Workshop"}

if __name__ == '__main__':
    app.run()