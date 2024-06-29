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
        # self.created_at = data['created_at']
        # self.updated_at = data['updated_at']
    
    @classmethod
    def save(cls,form):

        hashed_pw = bcrypt.generate_password_hash(form['password'])

        data = {
            **form,
            'password' : hashed_pw,
        }


        query = "INSERT INTO users(first_name,last_name,email,password) VALUES(%(first_name)s,%(last_name)s,%(email)s,%(password)s)"
        
        return connectToMySQL('users_login').query_db( query, data )
    
    @staticmethod
    def validate(data):

        is_valid = True

        if len(data['first_name']) < 2:
            is_valid = False
            flash('Name must be at least 2 characters!')
        if not str.isalpha(data['first_name']):
            is_valid = False
            flash('Name must not have any numbers!')
        if not str.isalpha(data['last_name']):
            is_valid = False
            flash('Name must not have any numbers!')
        if len(data['last_name']) < 2:
            is_valid = False
            flash('Name must be at 2 characters')
        if not EMAIL_REGEX.match(data['email']):
            is_valid = False
            flash('Not a valid email!')
        if len(data['password']) < 9:
            is_valid = False
            flash('Password must be at least 9 characters')
        if data['password'] != data['confirm_password']:
            is_valid = False
            flash('Passwords do not match!')
        
        return is_valid

    @classmethod
    def get_by_email(cls,email):

        data = {
            'email' : email
        }

        query = "SELECT * FROM users WHERE email = %(email)s;"
        results = connectToMySQL("users_login").query_db(query,data)
        # print(results)


        if results:
            user = cls(results[0])
            return user
        else:
            return False
    
    @classmethod
    def validate_email(cls,form):

        found_user = cls.get_by_email(form['email'])

        if found_user:
            if bcrypt.check_password_hash(found_user.password,form['password']):
                return found_user
            else:
                flash('Invalid Log In!')
                return False
        else:
            flash('Invalid Log In!')
            return False
