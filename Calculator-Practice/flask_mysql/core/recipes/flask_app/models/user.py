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
    def create_user(cls,form):

        hashed_pw = bcrypt.generate_password_hash(form['password'])

        data = {
            **form,
            'password' : hashed_pw
        }


        query = 'INSERT INTO users(first_name,last_name,email,password) VALUES(%(first_name)s,%(last_name)s,%(email)s,%(password)s)'

        return connectToMySQL("recipes").query_db(query,data)

    @staticmethod
    def validate(data):
        is_valid = True

        if len(data['first_name']) <  2:
            is_valid = False
            flash('First name must have more than 2 characters!')
        if len(data['last_name']) < 2:
            is_valid = False
            flash('Last name must have more than 2 characters!')
        if not EMAIL_REGEX.match(data['email']):
            is_valid = False
            flash('Not a valid email!')
        if data['password'] != data['confirm_pw']:
            is_valid = False
            flash('Passwords do not match!')
        if User.getbyemail(data['email']):
            is_valid = False
            flash('User already exists!')

        return is_valid

    @classmethod
    def getbyemail(cls,email):

        data = {
            'email' : email
        }

        query = 'SELECT * FROM users WHERE email = %(email)s'
        results = connectToMySQL("recipes").query_db(query,data)

        if results:
            user = cls(results[0])
            # print(user.password)
            # print(user.first_name)
            return user
        else:
            return False
        
    @classmethod
    def validate_by_email(cls,form):

        found_user = cls.getbyemail(form['email'])
        # print(found_user.password)
        # print(form['password'])
        if found_user:
            if bcrypt.check_password_hash(found_user.password,form['password']):
            # if True:
                return found_user
        
            else:
                flash('Invalid Login!')
                return False
        else:
            flash('Invalid Login!')
            return False