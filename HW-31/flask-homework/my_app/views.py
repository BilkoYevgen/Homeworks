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
    if request.args.get('size'):
        users = User.query.limit(int(request.args.get('size'))).all()
    else:
        users = User.query.all()
    return [{
        'id': user.id,
        'first_name': user.first_name,
        'last_name': user.last_name,
        'age': user.age
    } for user in users]

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
    if request.args.get('size'):
        books = Book.query.limit(int(request.args.get('size'))).all()
    else:
        books = Book.query.all()
    return [{
        'id': book.id,
        'title': book.title,
        'author': book.author,
        'year': book.year,
        'price': book.price,
    } for book in books]


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

@app.route('/purchases', methods=['GET'])
def get_purchases():
    if request.args.get('size'):
        purchases = Purchase.query.limit(int(request.args.get('size'))).all()
    else:
        purchases = Purchase.query.all()
    return [{
        'id': purchase.id,
        'user': {
            'id': purchase.user.id,
            'first_name': purchase.user.first_name,
            'last_name': purchase.user.last_name,
            'age': purchase.user.age,
        },
        'book': {
            'id': purchase.book.id,
            'title': purchase.book.title,
            'author': purchase.book.author,
            'year': purchase.book.year,
            'price': purchase.book.price
        },
        'date': purchase.date
    } for purchase in purchases]



@app.route('/purchases/<int:purchases_id>')
def purchase_id(purchases_id):
    purchase = Purchase.query.get(purchases_id)
    if purchase:
        purchase_data = {
            'id': purchase.id,
            'user_id': purchase.user_id,
            'book_id': purchase.book_id,
            'date': purchase.date,
            'title': purchase.book.title,
            'author': purchase.book.author,
            'first_name': purchase.user.first_name,
            'last_name': purchase.user.last_name,
            'age': purchase.user.age,
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