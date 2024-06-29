from flask_app import Flask
from flask_app.models.user import User
from flask_app.config.mysqlconnection import connectToMySQL
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
        self.updated_at = data['updated_at']

    @classmethod
    def getall(cls):
        
        query = "SELECT * FROM recipes JOIN users ON recipes.user_id = users.id"

        results = connectToMySQL('recipes').query_db(query)

        recipes = []

        if results:



            for row in results:
                user_recipe = cls(row)
                
                user_data = {
                    'id' : row['users.id'],
                    'first_name' : row['first_name'],
                    'last_name' : row['last_name'],
                    'email' : row['email'],
                    'password' : row['password'],
                    'created_at' : row['created_at'],
                    'updated_at': row['updated_at'],
                    'user_id' : row['user_id']
                }

                user_recipe.user = User(user_data)

                recipes.append(user_recipe)

        return recipes

    @staticmethod
    def validate_recipe(form):
        is_valid = True

        if len(form['recipe-name']) < 3:
            is_valid = False
            flash('Name must have more than 3 characters!')
        if len(form['description']) < 3:
            is_valid = False
            flash('Description must have more than 3 characters!')
        if len(form['instructions']) < 3:
            is_valid = False
            flash('Instructions must have more than 3 characters!')
        
        return is_valid
    
    @classmethod
    def create_recipe(cls,form):
        data = {
            'user_id' : session['uid'],
            'recipe_name' : form['recipe-name'],
            'description' : form['description'],
            'instructions' : form['instructions'],
            'date_made' : form['when'],
            'under_thirty' : form['under_thirty']
        }

        query = 'INSERT INTO recipes(user_id,recipe_name,description,instructions,date_made,under_thirty) VALUES(%(user_id)s,%(recipe_name)s,%(description)s,%(instructions)s,%(date_made)s,%(under_thirty)s)'
        
        return connectToMySQL('recipes').query_db( query, data )

    @classmethod
    def get_one_recipe(cls,data):
        query = 'SELECT * FROM recipes JOIN users ON users.id = recipes.user_id WHERE recipes.id = %(id)s' 

        results = connectToMySQL('recipes').query_db( query,data)

        if results:
            row = results[0]
            recipe = cls(row)
            user_data = {
                'id' : row['users.id'],
                'first_name' : row['first_name'],
                'last_name' : row['last_name'],
                'email' : row['email'],
                'password' : row['password'],
                'created_at' : row['users.created_at'],
                'updated_at' : row['users.updated_at'],
                'user_id'   : row['user_id']
            }
            recipe.maker = User(user_data)
            
            return recipe

    @classmethod
    def edit_recipe(cls,data):
        query = 'UPDATE recipes SET recipe_name = %(recipe_name)s, description = %(description)s, instructions= %(instructions)s,date_made = %(date_made)s,under_thirty = %(under_thirty)s WHERE recipes.id = %(id)s'
        return connectToMySQL('recipes').query_db( query, data )
    
    @classmethod
    def delete_recipe(cls,data):
        query = 'DELETE FROM recipes WHERE recipes.id = %(recipe.id)s'
        return connectToMySQL('recipes').query_db(query, data)