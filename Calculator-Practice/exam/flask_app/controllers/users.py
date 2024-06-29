from flask_app import app
from flask import render_template, request, redirect,session,flash
from flask_app.models.user import User
from flask_bcrypt import Bcrypt
# bcrypt = Bcrypt(app)

@app.route('/register', methods=['POST'])
def register():

    if not User.validate(request.form):
        return redirect('/')
    
    User.save(request.form)
    
    return redirect('/dashboard')

@app.route('/loggingin',methods=['POST'])
def loggin():

    user = User.validate_by_email(request.form)
    if not user:
        return redirect('/')
    
    session['uid'] = user.id
    session['first_name'] = user.first_name

    return redirect('/dashboard')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')
