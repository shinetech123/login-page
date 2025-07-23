from flask import Flask, render_template, request, redirect, url_for
import json
import os

app = Flask(__name__)
USER_FILE = 'users.json'

def load_users():
    if os.path.exists(USER_FILE):
        with open(USER_FILE, 'r') as f:
            return json.load(f)
    return []

def save_users(users):
    with open(USER_FILE, 'w') as f:
        json.dump(users, f, indent=4)

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    users = load_users()
    for user in users:
        if user['username'] == username and user['password'] == password:
            return render_template('dashboard.html', username=username)
    return render_template('login.html', error="Invalid credentials")

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        users = load_users()
        for user in users:
            if user['username'] == username:
                return render_template('register.html', error="Username already exists")
        users.append({"username": username, "password": password})
        save_users(users)
        return redirect(url_for('home'))
    return render_template('register.html')

@app.route('/forgot-password', methods=['GET', 'POST'])
def forgot_password():
    if request.method == 'POST':
        username = request.form['username']
        users = load_users()
        for user in users:
            if user['username'] == username:
                return render_template('forgot_password.html', password=user['password'], show=True)
        return render_template('forgot_password.html', error="User not found")
    return render_template('forgot_password.html', show=False)

if __name__ == '__main__':
    app.run(debug=True)
