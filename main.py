from flask import Flask, render_template

app = Flask(__name__)

datas = [
    {
        'app': 'Facebook',
        'username': 'Panas',
        'email': 'panas@demo.com',
        'password': 'facebookpassword'
    },
    {
        'app': 'Gmail',
        'username': 'Panas18',
        'email': 'panas2@demo.com',
        'password': 'gmailPassword',

    }
]


@app.route('/')
def home():
    return render_template('home.html', title='Home', datas=datas)


@app.route('/account')
def account():
    return render_template('account.html', title="Account")


@app.route('/add')
def add():
    return render_template('add.html', title="Account")


@app.route('/logout')
def logout():
    return render_template('logout.html', title="Account")


@app.route('/login')
def login():
    return render_template('login.html', title="Account")


@app.route('/register')
def register():
    return render_template('register.html', title="Account")


if __name__ == "__main__":
    app.run(debug=True)
