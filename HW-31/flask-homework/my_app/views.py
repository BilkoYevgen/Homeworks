from flask import request, redirect, session, render_template, url_for, abort
from . import app
from .models import User, Book, Purchase

app.secret_key = app.config.get('SECRET_KEY')

@app.route('/')
def index():
    name = session.get('name')
    app.logger.info("This INFO request")
    app.logger.error("This ERROR request")
    if name:
        return render_template('index.html', name=name)
    else:
        return redirect(url_for('login'))

@app.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return [{
        'id': user.id,
        'first_name': user.first_name,
        'last_name': user.last_name,
        'age': user.age
    } for user in users][:int(request.args.get('size')) if 'size' in request.args else None]

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user_by_id(user_id):
    user = User.query.get(user_id)
    if user:
        user_data = {
            'id': user.id,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'age': user.age
        }
        return user_data
    else:
        abort(404)

@app.route('/books', methods=['GET'])
def get_books():
    all_books = Book.query.all()
    dict_books = []
    for book in all_books:
        dict_books.append({
            'id': book.id,
            'title': book.title,
            'author': book.author,
            'year': book.year,
            'price': book.price,
        })
    if 'size' in request.args:
        size = int(request.args.get('size'))
        return dict_books[:size]
    else:
        return dict_books

@app.route('/books/<int:book_id>', methods=['GET'])
def get_book_by_title(book_id):
    book = Book.query.get(book_id)
    if not book:
        return abort(404)
    book_data = {
        'id': book.id,
        'title': book.title,
        'author': book.author,
        'year': book.year,
        'price': book.price
    }
    return book_data

@app.route('/purchases')
def get_purchases():
    purchases = Purchase.query.all()
    result = []
    for purchase in purchases:
        book = Book.query.get(purchase.book_id)
        user = User.query.get(purchase.user_id)
        purchase_info = {
            'id': purchase.id,
            'user': {
                'id': user.id,
                'first_name': user.first_name,
                'last_name': user.last_name,
                'age': user.age,
            },
            'book': {
                'id': book.id,
                'title': book.title,
                'author': book.author,
                'year': book.year,
                'price': book.price
            },
            'date': purchase.date
        }
        result.append(purchase_info)
    if 'limit' in request.args:
        limit = int(request.args['limit'])
        return result[:limit]
    return result

@app.route('/purchases/<int:purchases_id>')
def purchase_id(purchases_id):
    purchase = Purchase.query.get(purchases_id)
    if purchase:
        book = Book.query.get(purchase.book_id)
        user = User.query.get(purchase.user_id)
        purchase_data = {
            'id': purchase.id,
            'user_id': purchase.user_id,
            'book_id': purchase.book_id,
            'date': purchase.date,
            'title': book.title,
            'author': book.author,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'age': user.age,
        }
        return purchase_data
    return abort(404)

@app.route('/params', methods=['GET'])
def get_params():
    if 'name' in session:
        name = session['name']
        params = request.args.items()
        params_table = '<table><tr><th>parameter</th><th>value</th></tr>'
        for key, value in params:
            params_table += f'<tr><td>{key}</td><td>{value}</td></tr>'
        params_table += '</table>'
        return render_template('params.html', params_table=params_table, name=name)
    else:
        return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        name = request.form.get('name')
        session['name'] = name
        return redirect(url_for('index'))
    else:
        return render_template('login.html')