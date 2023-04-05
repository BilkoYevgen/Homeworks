from my_app import app
import random
import secrets
from flask import request, redirect, session, render_template, url_for

app.secret_key = secrets.token_hex(16)

@app.route('/')
def index():
    name = session.get('name')
    if name:
        return render_template('index.html', name=name)
    else:
        return redirect(url_for('login'))

@app.route('/users', methods=['GET'])
def get_users():
    if 'name' in session:
        all_names = ['Alice', 'Bob', 'Charlie', 'David', 'Eva', 'Frank', 'Grace', 'Henry', 'Ivy', 'Jack', 'Karen', 'Luke', 'Megan', 'Nancy', 'Oliver', 'Paul', 'Quinn', 'Rachel', 'Sam', 'Tina', 'Victor', 'Wendy', 'Xavier', 'Yolanda', 'Zack']
        random_names = random.sample(all_names, 10)
        return render_template('users.html', name=session['name'], names=random_names)
    else:
        return redirect(url_for('login'))
@app.route('/books', methods=['GET'])
def get_books():
    if 'name' in session:
        # Generate a list of 10 random books
        all_books = ['1984 by George Orwell', 'To Kill a Mockingbird by Harper Lee', 'Pride and Prejudice by Jane Austen', 'The Catcher in the Rye by J.D. Salinger', 'The Great Gatsby by F. Scott Fitzgerald', 'Brave New World by Aldous Huxley', 'One Hundred Years of Solitude by Gabriel Garcia Marquez', 'The Lord of the Rings by J.R.R. Tolkien', 'Animal Farm by George Orwell', 'The Diary of a Young Girl by Anne Frank', 'The Hitchhiker\'s Guide to the Galaxy by Douglas Adams', 'The Hunger Games by Suzanne Collins']
        random_books = random.sample(all_books, 10)
        return render_template('books.html', name=session['name'], books=random_books)
    else:
        return redirect(url_for('login'))
@app.route('/users/<int:id>', methods=['GET'])
def get_user_by_id(id):
    if 'name' in session:
        if id % 2 == 0:
            name = session['name']
            return render_template('user.html', id=id, name=name)
        else:
            return 'Not found', 404
    else:
        return redirect(url_for('login'))

@app.route('/books/<title>', methods=['GET'])
def get_book_by_title(title):
    if 'name' in session:
        name = session['name']
        transformed_title = title.capitalize()
        return render_template('book.html', transformed_title=transformed_title, name=name)
    else:
        return redirect(url_for('login'))


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