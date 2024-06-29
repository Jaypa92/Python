from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.user import User
from flask_app.models.recipe import Recipe
from flask_bcrypt import Bcrypt

@app.route('/')
def index():
        
    return render_template('index.html')

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

@app.route('/dashboard')
def dashboard():

    if 'uid' not in session:
        flash('User must be logged in!')
        redirect('/')

    return render_template('dashboard.html',recipes = Recipe.getall())

@app.route('/create')
def create():

    if 'uid' not in session:
        flash('User must be logged in!')
        return redirect('/')

    return render_template('add.html')

@app.route('/create_recipe',methods=['POST'])
def create_recipe():

    recipe = Recipe.recipe_validate(request.form)

    if not recipe:
    
        return redirect('/create')
    
    Recipe.save(request.form)

    return redirect('/dashboard')

@app.route('/view_recipe')
def view_recipe():

    if 'uid' not in session:
        flash('Must be logged in!')
        return redirect('/')
    
    data = {
        'id' : session['uid']
    }

    return render_template('view_recipe.html',users = Recipe.get_one(data))
@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

