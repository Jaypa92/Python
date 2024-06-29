from flask_app import Flask
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.user import User
from flask import flash,session

class Car:

    def __init__(self,data):
        self.id = data['id']
        self.user_id = data['users_id']
        self.make = data['make']
        self.model = data['model']
        self.year = data['year']
        self.price = data['price']
        self.description = data['description']
        self.created_at = data['created_at']
        self.updated_at = data['created_at']

    @staticmethod
    def car_validate(form):
            print(form)
            is_valid = True
            if len(form['price']) < 1:
                flash('Invalid Field Option!')
                is_valid = False
            if len(form['model']) < 1:
                flash('All fields Required!')
                is_valid = False
            if len(form['make']) < 1:
                flash('All fields required!')
                is_valid = False
            if len(form['year']) < 1:
                flash('All fields required!')
                is_valid = False
            if len(form['description']) < 1:
                flash('All fields required!')
                is_valid = False

            return is_valid
    @classmethod
    def save(cls,form):

        data = {
            'users_id' : session['uid'],
            'price' : form['price'],
            'model' : form['model'],
            'make' : form['make'],
            'year' : form['year'],
            'description' : form['description']

        }

        query = 'INSERT INTO cars(users_id,price,model,make,year,description) VALUES(%(users_id)s,%(price)s,%(model)s,%(make)s,%(year)s,%(description)s)'
        return connectToMySQL("car_dealz").query_db(query,data)
    
    @classmethod
    def getall(cls):
        query = 'SELECT * FROM cars JOIN users ON users.id = cars.users_id'
        results = connectToMySQL('car_dealz').query_db(query)

        cars = []

        if results:
            for row in results:
                car = cls(row)

                user_data = {
                    'id' : row['users.id'],
                    'first_name' : row['first_name'],
                    'last_name' : row['last_name'],
                    'email' : row['email'],
                    'password' : row['password'],
                    'created_at' : row['users.created_at'],
                    'updated_at' : row['users.updated_at'],
                    'users_id' : row['users_id']
                }

                car.user = User(user_data)

                cars.append(car)
        return cars
    
    @classmethod
    def get_one(cls,data):
        query = 'SELECT * FROM cars JOIN users ON users.id = cars.users_id WHERE cars.id = %(id)s' 

        results = connectToMySQL('car_dealz').query_db( query,data)

        if results:
            row = results[0]
            car = cls(row)
            user_data = {
                'id' : row['users.id'],
                'first_name' : row['first_name'],
                'last_name' : row['last_name'],
                'email' : row['email'],
                'password' : row['password'],
                'created_at' : row['users.created_at'],
                'updated_at' : row['users.updated_at'],
                'user_id'   : row['users_id']
            }
            car.user = User(user_data)
            
            return car

    @classmethod
    def edit_car(cls,data):
        query = 'UPDATE cars SET make = %(make)s, model = %(model)s, year = %(year)s,price = %(price)s,description = %(description)s WHERE cars.id = %(id)s'
        return connectToMySQL('car_dealz').query_db( query, data )
    
    @classmethod
    def delete_car(cls,data):
        query = 'DELETE FROM cars WHERE cars.id = %(cars.id)s'
        return connectToMySQL('car_dealz').query_db(query, data)