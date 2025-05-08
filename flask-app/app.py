from flask import Flask, render_template_string, request, redirect, url_for, session
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("APP_SECRET_KEY")

USERNAME = os.getenv("APP_USERNAME")
PASSWORD = os.getenv("APP_PASSWORD")


@app.route('/')
def index():
    if 'user' in session:
        return f"Welcome {session['user']}!"
    return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if request.form['username'] == USERNAME and request.form['password'] == PASSWORD:
            session['user'] = USERNAME
            return redirect(url_for('index'))
        return "Invalid credentials", 401
    return render_template_string(
        '<form method="post">Username: <input name="username">'
        ' Password: <input name="password" type="password">'
        ' <input type="submit"></form>'
    )


@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('login'))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

