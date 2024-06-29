from flask_app import app
from flask import render_template, request, redirect,session,flash
from flask_app.models.user import User
from flask_app.models.car import Car
from flask_bcrypt import Bcrypt
# bcrypt = Bcrypt(app)

@app.route('/')
def index():

    return render_template('index.html')

@app.route('/dashboard')
def dashboard():
    if 'uid' not in session:
        return redirect('/')
    return render_template('dashboard.html',cars = Car.getall())

@app.route('/create')
def create():

    if 'uid' not in session:
        flash('User must be logged in!')
        return redirect('/')

    return render_template('add.html')

@app.route('/create_car',methods=['POST'])
def create_recipe():

    car = Car.car_validate(request.form)

    if not car:
    
        return redirect('/create')
    
    Car.save(request.form)

    return redirect('/dashboard')

@app.route('/view/<int:car_id>')
def view_car(car_id):

    if 'uid' not in session:
        flash('Must be logged in!')
        return redirect('/')
    
    data = {
        'id' : car_id
    }

    return render_template('view.html',cars = Car.get_one(data))

@app.route('/edit_car/<int:car_id>')
def edit_recipe(car_id):
    if 'uid' not in session:
        flash('Must be logged in!')
        return redirect ('/')
    

    data= {
        'id' : car_id
    }
    
    return render_template('edit.html', cars = Car.get_one(data) )

@app.route('/editting',methods=['POST'])
def process_edit():
    
    new_car = Car.car_validate(request.form)

    if not new_car:
        
        return redirect(f'/edit_car/{request.form["id"]}')

    data = {
        'id' : request.form['id'],
        'make' : request.form['make'],
        'model' : request.form['model'],
        'year' : request.form['year'],
        'price' : request.form['price'],
        'description' : request.form['description']
    }

    Car.edit_car(data)

    return redirect('/dashboard')

@app.route('/delete_car/<int:car_id>')
def delete(car_id):

    data={
        'cars.id' : car_id
    }
    Car.delete_car(data)

    return redirect('/dashboard')