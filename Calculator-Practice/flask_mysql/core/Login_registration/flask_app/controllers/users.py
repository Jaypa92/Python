from flask_app import app
from flask import render_template, request, redirect,session,flash
from flask_app.models.user import User
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route('/')
def index():
    
    return render_template('login_registration_index.html')

@app.route('/hey_user')
def hey():

    if 'user-id' not in session:
        flash('Need to log in')
        return redirect('/')
    
    return render_template('hey_user.html')

@app.route('/processing',methods=["POST"])
def process():
    if not User.validate(request.form):
        return redirect('/')
    # data= {
    #     'first_name' : request.form['first_name'],
    #     'last_name' : request.form['last_name'],
    #     'email' : request.form['email'],
    #     'password' : request.form['password']
    # }

    User.save(request.form)

    return redirect('/')

@app.route('/logging-in',methods=['POST'])
def login():

    uid = User.validate_email(request.form)
    
    if not uid:
        return redirect('/')

    session['user-id'] = uid.id
    session['first_name'] = uid.first_name

    return redirect('/hey_user')

@app.route('/logout')
def logout():

    session.clear()

    return redirect('/')