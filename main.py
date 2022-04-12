from flask import Flask, render_template, redirect, request
from data import db_session
from data.users import User
from data.jobs import Jobs
import requests
from bs4 import BeautifulSoup
from data.forms import RegisterForm, LoginForm, WorksForm
from flask_login import LoginManager, login_user, logout_user, login_required
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(id)

@app.route("/")
def index():
    session = db_session.create_session()
    jobs = session.query(Jobs).all()
    return render_template("index.html", jobs=jobs)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect("/")
        return render_template('login.html',
                               message="Неправильный логин или пароль",
                               form=form)
    return render_template('login.html', title='Авторизация', form=form)


@app.route('/register', methods=['GET', 'POST'])
def reqister():
    form = RegisterForm()
    if form.validate_on_submit():
        if form.password.data != form.confirm.data:
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Пароли не совпадают")
        db_sess = db_session.create_session()
        if db_sess.query(User).filter(User.email == form.login.data).first():
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Такой пользователь уже есть")
        user = User(
            name=form.name.data,
            surname=form.surname.data,
            email=form.login.data
        )
        user.set_password(form.password.data)
        db_sess.add(user)
        db_sess.commit()
        return redirect('/login')
    return render_template('register.html', title='Регистрация', form=form)


@app.route('/subjects', methods=['GET', 'POST'])
def subjects():
    return render_template('subjects.html')


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/")


def last_news(channel_name):
    tgurl = 'https://t.me/s/'
    url = tgurl + channel_name
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'lxml')
    link = soup.find_all('a')
    url = link[-1]['href']
    url = url.replace('https://t.me/', '')
    channel_name, news_id = url.split('/')
    urls = []
    for i in range(5):
        urls.append(f'{channel_name}/{int(news_id) - i}')
    return urls


@app.route('/bot', methods=['POST', 'GET'])
def main_page():
    url = 'free_edu/5073'
    if request.method == 'GET':
        return render_template('tgbot.html', url=url)
    else:
        channel_name = request.form['adress']
        urls = last_news(channel_name)
        return render_template('tgbot.html', urls=urls)


def main():
    name_db = 'mars_explorer.db'
    db_session.global_init(f"db/{name_db}")
    app.run(port=5000, host='127.0.0.1')


if __name__ == '__main__':
    main()
