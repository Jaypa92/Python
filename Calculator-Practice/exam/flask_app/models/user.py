from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL
import re
from flask import flash
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class User:
    def __init__(self,data):

        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def getbyemail(cls,email):

        data = {
            'email' : email
        }

        query = 'SELECT * FROM users WHERE email = %(email)s'
        print(email)

        results = connectToMySQL("car_dealz").query_db(query,data)

        if results:
            user = cls(results[0])
            return user
        else:
            return False
    
    @staticmethod
    def validate(form):
        is_valid = True

        if len(form['first_name']) < 3:
            flash('First Name must be more than 3 characters!')
            is_valid = False
        if len(form['last_name']) < 3:
            flash('Last Name must be more than 3 characters!')
            is_valid = False
        if not EMAIL_REGEX.match(form['email']):
            flash('Not a valid email!')
            is_valid = False
        if len(form['password']) < 8:
            flash('Password must be at least 8 characters!')
            is_valid = False
        if form['password'] != form['confirm_pw']:
            flash('Passwords must match!')
            is_valid = False
        if User.getbyemail(form['email']):
            flash('User already exists!')
            is_valid = False

        return is_valid
    
    @classmethod
    def save(cls,form):

        hashed_pw = bcrypt.generate_password_hash(form['password'])

        data = {
            **form,
            'password' : hashed_pw
        }

        query = 'INSERT INTO users(first_name,last_name,email,password) VALUES(%(first_name)s,%(last_name)s,%(email)s,%(password)s)'

        return connectToMySQL("car_dealz").query_db(query,data)
    
    @classmethod
    def validate_by_email(cls,form):

        found_user = User.getbyemail(form['email'])

        if found_user:
            if bcrypt.check_password_hash(found_user.password,form['password']):
                return found_user
            else:
                flash('Invalid login!')
                return False
        else:
            flash('Invalid login!')
            return False
        