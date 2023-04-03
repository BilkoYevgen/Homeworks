from my_app import app
import random
from flask import request, redirect, make_response

@app.route('/hello')
def index():
    app.logger.info("This INFO request")
    app.logger.error("This ERROR request")
    return "Hello, world!"

@app.route('/users', methods=['GET'])
def get_users():
    users = ['John', 'Jane', 'Mike', 'Sara', 'Tom']
    return random.sample(users, k=random.randint(1, len(users)))

@app.route('/books', methods=['GET'])
def get_books():
    books = ['The Great Gatsby', 'To Kill a Mockingbird', 'One Hundred Years of Solitude', 'Pride and Prejudice', '1984']
    books_html = '<ul>'
    for book in random.sample(books, k=random.randint(1, len(books))):
        books_html += f'<li>{book.title()}</li>'
    books_html += '</ul>'
    return books_html

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    if user_id % 2 == 0:
        return f'The user id is {user_id}'
    else:
        return 'Not Found', 404

@app.route('/books/<string:title>', methods=['GET'])
def get_book(title):
    return title.title()


@app.route('/params', methods=['GET'])
def get_params():
    table = "<table><tr><th>parameter</th><th>value</th></tr>"
    for key, value in request.args.items():
        table += f"<tr><td>{key}</td><td>{value}</td></tr>"
    table += "</table>"
    return table, 200

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        form = '<form method="POST" action="/login"><input type="text" name="username"><input type="password" name="password"><input type="submit" value="Submit"></form>'
        return form
    elif request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if username and password:
            return redirect('/users')
        else:
            return make_response('Missing username or password', 400)