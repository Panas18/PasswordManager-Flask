from flask import Flask, render_template, url_for
from form import RegistrationForm, LoginForm
import os


app = Flask(__name__)

app.config['SECRET_KEY'] = os.environ['SECRET_KEY']

datas = [
    {
        'app': 'Facebook',
        'username': 'Panas',
        'email': 'panas@demo.com',
        'url': "www.facebook.com",
        'password': 'facebookpassword',
        'type': 'login',
        'date_posted': '2019-2-3'
    },
    {
        'app': 'Gmail',
        'username': 'Panas18',
        'url': 'www.google.com',
        'email': 'panas2@demo.com',
        'password': 'gmailPassword',
        'type': 'login',
        'date_posted': '2020-4-8'

    }
]


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title='Home', datas=datas)


@app.route('/account')
def account():
    return render_template('account.html', title="Account")


@app.route('/logout')
def logout():
    return render_template('logout.html', title="logout")


@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title="Login", form=form)


@app.route('/register', methods=['GET', 'POST'] )
def register():
    form = RegistrationForm()
    return render_template('register.html', title="Register", form=form)


if __name__ == "__main__":
    app.run(debug=True)
