from flask_app import Flask
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.user import User
from flask import flash,session


class Recipe:

    def __init__(self,data):
        self.id = data['id']
        self.user_id = data['user_id']
        self.recipe_name = data['recipe_name']
        self.description = data['description']
        self.instructions = data['instructions']
        self.date_made = data['date_made']
        self.under_thirty = data['under_thirty']
        self.created_at = data['created_at']
        self.updated_at = data['created_at']

    @staticmethod
    def recipe_validate(form):
        print(form)
        is_valid = True
        if len(form['recipe_name']) < 3:
            flash('Name must be more than 3 characters!')
            is_valid = False
        if len(form['description']) < 3:
            flash('Must be at least 3 characters!')
            is_valid = False
        if len(form['instructions']) < 3:
            flash('Must be at least 3 characters!')
            is_valid = False
        if len(form['date_made']) < 1:
            flash('All fields required!')
            is_valid = False
        if 'under_thirty' not in form:
            flash('All fields required!')
            is_valid = False

        return is_valid
        
    @classmethod
    def save(cls,form):

        data = {
            'user_id' : session['uid'],
            'recipe_name' : form['recipe_name'],
            'description' : form['description'],
            'instructions' : form['instructions'],
            'date_made' : form['date_made'],
            'under_thirty' : form['under_thirty']
        }

        query = 'INSERT INTO recipes(user_id,recipe_name,description,instructions,date_made,under_thirty) VALUES(%(user_id)s,%(recipe_name)s,%(description)s,%(instructions)s,%(date_made)s,%(under_thirty)s)'
        return connectToMySQL("recipes").query_db(query,data)
    
    @classmethod
    def getall(cls):
        query = 'SELECT * FROM recipes JOIN users ON users.id = recipes.user_id'
        results = connectToMySQL('recipes').query_db(query)

        recipes = []

        if results:
            for row in results:
                recipe = cls(row)

                user_data = {
                    'id' : row['users.id'],
                    'first_name' : row['first_name'],
                    'last_name' : row['last_name'],
                    'email' : row['email'],
                    'password' : row['password'],
                    'created_at' : row['users.created_at'],
                    'updated_at' : row['users.updated_at'],
                    'user_id' : row['user_id']
                }

                recipe.user = User(user_data)

                recipes.append(recipe)
        return recipes
    
    @classmethod
    def get_one(cls,data):

        query = 'SELECT * FROM users JOIN recipes ON users.id = recipes.user_id WHERE users.id = %(id)s'
        results = connectToMySQL('recipes').query_db(query,data)


        if results:
            user = User(results[0])
            user.recipes = []
            for row in results:
                recipe_data = {
                        'id' : row['recipes.id'],
                        'recipe_name' : row['recipe_name'],
                        'description' : row['description'],
                        'instructions' : row['instructions'],
                        'date_made' : row['date_made'],
                        'under_thirty' : row['under_thirty'],
                        'user_id' : row['user_id'],
                        'created_at' : row['recipes.created_at'],
                        'updated_at' : row['recipes.updated_at'],
                    }

                recipe=Recipe(recipe_data)

                user.recipes.append(recipe)
            
        return user
