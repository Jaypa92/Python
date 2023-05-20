from flask_app import app
from flask import render_template,redirect,request,session
from flask_app.models.user import User
from flask_app.models.post import Post
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route('/')
def start():

    return render_template('intro.html')

@app.route('/no')
def no():
    return render_template('no_prescription.html')

@app.route('/index')
def index():

    return render_template('index.html')

@app.route('/create_newbie', methods=['POST'])
def create():

    if not User.validate(request.form):
        return redirect('/index')
    
    User.save(request.form)

    return redirect('/dashboard')

@app.route('/dashboard')
def main():

    if 'uid' not in session:
        return redirect('/index')

    return render_template('dashboard.html',posts = Post.getall()) 

@app.route('/logging_in',methods=['POST'])
def login():

    user = User.validate_by_email(request.form)
    if not user:
        return redirect('/index')
    
    session['first_name'] = user.first_name
    session['uid'] = user.id

    return redirect('/dashboard')

@app.route('/make_post',methods=['POST'])
def make():

    post = Post.validate(request.form)

    if not post:
        return redirect('/dashboard')

    Post.create(request.form)

    return redirect('/dashboard')

@app.route('/delete/<int:post_id>')
def delete(post_id):

    data = {
            'id' : post_id
        }

    Post.delete(data)

    return redirect('/dashboard')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/index')
