from flask import render_template, url_for, flash, redirect, request
from pasman import app, db
from pasman.models import User, Post
from pasman.forms import RegistrationForm, LoginForm


posts = [
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
    return render_template('home.html', title='Home', posts=posts)


@app.route('/account')
def account():
    return render_template('account.html', title="Account")


@app.route('/logout')
def logout():
    return redirect(url_for('login'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if request.method == "POST" and form.validate():
        user = User(username=form.username.data,
                    email=form.email.data,
                    password=form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route('/login', methods=["GET", "POST"])
def login():
    form = LoginForm()
    if request.method == "POST" and form.validate():
        user = User.query.filter_by(email=form.email.data).first()
        if user:
            if user.password == form.password.data:
                flash("login is successful", 'success')
                return redirect(url_for('home'))
            else:
                flash("Your password is incorrect. Please try again!", 'danger')
                return redirect(url_for('login'))
        else:
            flash("Your email is not registeres on our database", 'danger')
            return redirect(url_for('login')) 
    return render_template('login.html', title="Login", form=form)
