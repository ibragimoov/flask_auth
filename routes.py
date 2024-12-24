from flask import render_template, request, redirect, url_for
from flask_login import current_user, login_user, logout_user, login_required

from models import User


def register_routes(app, db, bcrypt):

    @app.route('/')
    def index():
        return render_template('index.html', current_user=current_user)

    @app.route('/signup', methods=['GET', 'POST'])
    def signup():
        if request.method == 'GET':
            return render_template('signup.html')
        elif request.method == 'POST':
            username = request.form['username']
            password = request.form['password']

            hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

            new_user = User(username=username, password=hashed_password, role='user')

            db.session.add(new_user)
            db.session.commit()

            return redirect(url_for('index'))

    @app.route('/signin', methods=['GET', 'POST'])
    def signin():
        if request.method == 'GET':
            return render_template('signin.html')
        elif request.method == 'POST':
            username = request.form['username']
            password = request.form['password']

            user = User.query.filter(User.username == username).first()

            if bcrypt.check_password_hash(user.password, password):
                login_user(user)
                redirect(url_for('index'))
            else:
                return 'Неверный логин или пароль'

            return redirect(url_for('index'))