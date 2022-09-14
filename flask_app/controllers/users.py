from flask import render_template, request, redirect
from flask_app import app
from flask_app.models.user import User

@app.route('/')
@app.route('/home')
def home():
    return redirect('/users')

@app.route('/users/')
def users():
    return render_template('users.html', users=User.get_all())

@app.route('/user/new')
def new():
    return render_template('add_user.html')

@app.route('/user/create', methods=['POST'])
def create():
    print(request.form)
    User.save(request.form)
    return redirect('/users')
