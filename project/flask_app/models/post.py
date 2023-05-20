from flask_app.config.mysqlconnection import connectToMySQL
from flask import app, session,flash
from flask_app.models.user import User

class Post:
    def __init__(self,data):
        self.id = data['id']
        self.post = data['post']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.users_id = data['users_id']

    @classmethod
    def create(cls,form):
        print(session['uid'])
        data = {
            'post': form['post'],
            'users_id' : session['uid']
        }

        query = 'INSERT INTO posts(post,users_id) VALUES(%(post)s,%(users_id)s)'
        return connectToMySQL("anti-depressant").query_db(query,data)
    
    @classmethod
    def validate(self,form):

        is_valid= True

        if len(form['post']) < 1:
            is_valid = False
            flash('Invalid input!')
        
        return is_valid
    
    @classmethod
    def getall(cls):
        query = 'SELECT * FROM posts JOIN users ON users.id = posts.users_id ORDER BY posts.created_at DESC'
        results = connectToMySQL('anti-depressant').query_db(query)

        posts = []

        if results:
            for row in results:
                post = cls(row)
                user_data = {
                    'id' : row['users.id'],
                    'first_name' : row['first_name'],
                    'last_name' : row['last_name'],
                    'email' : row['email'],
                    'password' : row['password'],
                    'created_at': row['users.created_at'],
                    'updated_at' : row['users.updated_at'],
                    'users_id' : row['users_id']
                }
                post.user = User(user_data)
                posts.append(post)
        return posts
    
    @classmethod
    def delete(cls,data):

        query = 'DELETE FROM posts WHERE id = %(id)s'

        return connectToMySQL("anti-depressant").query_db(query,data)