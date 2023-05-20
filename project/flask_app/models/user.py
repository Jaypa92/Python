from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re
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

    @staticmethod
    def validate(form):
        is_valid = True

        if len(form['first_name']) < 1:
            is_valid = False
            flash('Field must not be blank!')
        if len(form['last_name']) < 1:
            is_valid = False
            flash('Field must not be left blank!')
        if not EMAIL_REGEX.match(form['email']):
            is_valid = False
            flash('Invalid Email!')
        if len(form['password']) < 8:
            is_valid = False
            flash('Password must be 8 characteers!')
        if form['password'] != form['confirm_password']:
            is_valid = False
            flash('Passwords must match!')
        if User.getbyemail(form['email']):
            is_valid = False
            flash('User already exists!')

        return is_valid
    
    @classmethod
    def getbyemail(cls,email):

        data = {
            'email' : email
        }

        query = 'SELECT * FROM users WHERE email = %(email)s'
        results = connectToMySQL("anti-depressant").query_db(query,data)

        if results:
            user = cls(results[0])
            return user
        else:
            return False
    
    @classmethod
    def save(cls,form):

        hashed_pw = bcrypt.generate_password_hash(form['password'])

        data = {
            **form,
            'password' : hashed_pw
        }

        query = 'INSERT INTO users(first_name,last_name,email,password) VALUES(%(first_name)s,%(last_name)s,%(email)s,%(password)s)'
        return connectToMySQL("anti-depressant").query_db(query,data)
    
    @classmethod
    def validate_by_email(self,form):

        found_user = User.getbyemail(form['email'])
        print(found_user)

        if found_user:
            if bcrypt.check_password_hash(found_user.password,form['password']):
                return found_user
            else:
                flash('Invalid login!')
                return False
        else:
            flash('Invalid login!')
            return False
        
