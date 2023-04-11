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
    all_users = User.query.all()
    dict_users = [{
        'id': user.id,
        'first_name': user.first_name,
        'last_name': user.last_name,
        'age': user.age
    } for user in all_users]
    if 'size' in request.args:
        return dict_users[:int(request.args.get('size'))]
    return dict_users

@app.route('/books', methods=['GET'])
def get_books():
    all_books = Book.query.all()
    dict_books = [{
        'id': book.id,
        'title': book.title,
        'author': book.author,
        'year': book.year,
        'price': book.price
    } for book in all_books]
    if 'size' in request.args:
        return dict_books[:int(request.args.get('size'))]
    return dict_books

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user_by_id(user_id):
    all_users = User.query.all()
    for user in all_users:
        if user.id == user_id:
            user1 = [{
                'id': user.id,
                'first_name': user.first_name,
                'last_name': user.last_name,
                'age': user.age
            }]
            return user1
    return abort(404)

@app.route('/books/<int:book_id>', methods=['GET'])
def get_book_by_title(book_id):
    all_books = Book.query.all()
    for book in all_books:
        if book.id == book_id:
            book1 = [{
                'id': book.id,
                'title': book.title,
                'author': book.author,
                'year': book.year,
                'price': book.price
            }]
            return book1
    return abort(404)

@app.route('/purchase')
def purchase():
    all_purchase = Purchase.query.all()
    dict_purchase = []
    for purchase_1 in all_purchase:
        all_books = Book.query.all()
        book1 = [book for book in all_books if purchase_1.book_id == book.id]
        all_users = User.query.all()
        user1 = [user for user in all_users if purchase_1.user_id == user.id]
        purchase_2 = {
            'id': purchase_1.id,
            'user_id': purchase_1.user_id,
            'book_id': purchase_1.book_id,
            'date': purchase_1.date,
            'title': book1[0].title,
            'first_name': user1[0].first_name,
            'last_name': user1[0].last_name
        }
        dict_purchase.append(purchase_2)
    if 'size' in request.args:
        return dict_purchase[:int(request.args.get('size'))]
    return dict_purchase

@app.route('/purchase/<int:purchases_id>')
def purchase_id(purchases_id):
    all_purchase = Purchase.query.all()
    for purchase1 in all_purchase:
        if purchase1.id == purchases_id:
            all_books = Book.query.all()
            book1 = [book for book in all_books if purchase1.book_id == book.id]
            all_users = User.query.all()
            user1 = [user for user in all_users if purchase1.user_id == user.id]
            purchase_1 = [{
                'id': purchase1.id,
                'user_id': purchase1.user_id,
                'book_id': purchase1.book_id,
                'date': purchase1.date,
                'title': book1[0].title,
                'first_name': user1[0].first_name,
                'last_name': user1[0].last_name
            }]
            return purchase_1
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