from flask_app import app
from flask import render_template, request, redirect,session,flash
from flask_app.models.user import User
from flask_app.models.recipe import Recipe
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route('/')
def index():
    return render_template('recipes_index.html')

@app.route('/create-account',methods=['POST'])
def create():

    if not User.validate(request.form):
        return redirect('/')
    
    User.create_user(request.form)

    user = User.validate_by_email(request.form)

    session['uid'] = user.id

    return redirect('/welcome')

@app.route('/logging_in',methods=['POST'])
def login():

    user = User.validate_by_email(request.form)

    if not user:
        return redirect('/')
    session['uid'] = user.id
    session['first_name'] = user.first_name
    return redirect('/welcome')

@app.route('/welcome')
def welcome():
    if 'uid' not in session:
        flash('Must be logged in!')
        return redirect ('/')

    return render_template('welcome.html',recipes = Recipe.getall())

@app.route('/add-recipe')
def add_recipe():
    if 'uid' not in session:
        flash('Must be logged in!')
        return redirect ('/')
    return render_template('create.html')

@app.route('/create-recipe',methods=['POST'])
def create_recipe():
    recipe = Recipe.validate_recipe(request.form)

    if not recipe:
        return redirect('/add-recipe')
    Recipe.create_recipe(request.form)

    return redirect('/welcome')

@app.route('/view-recipe/<int:recipe_id>')
def view_recipe(recipe_id):
        if 'uid' not in session:
            flash('Must be logged in!')
            return redirect ('/')
        
        data = {
            'id' : recipe_id
        }
        return render_template('single_recipe.html',recipe = Recipe.get_one_recipe(data))

@app.route('/edit-recipe/<int:recipe_id>')
def edit_recipe(recipe_id):
    if 'uid' not in session:
        flash('Must be logged in!')
        return redirect ('/')


    data= {
        'id' : recipe_id
    }
    
    return render_template('edit.html', recipe = Recipe.get_one_recipe(data) )

@app.route('/editting',methods=['POST'])
def process_edit():
    
    new_recipe = Recipe.validate_recipe(request.form)

    if not new_recipe:
        
        return redirect(f'/edit-recipe/{request.form["id"]}')

    data = {
        'id' : request.form['id'],
        'recipe_name' : request.form['recipe-name'],
        'description' : request.form['description'],
        'instructions' : request.form['instructions'],
        'date_made' : request.form['when'],
        'under_thirty' : request.form['under_thirty']
    }

    Recipe.edit_recipe(data)

    return redirect('/welcome')

@app.route('/delete-recipe/<int:recipe_id>')
def delete(recipe_id):

    data={
        'recipe.id' : recipe_id
    }
    Recipe.delete_recipe(data)

    return redirect('/welcome')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)