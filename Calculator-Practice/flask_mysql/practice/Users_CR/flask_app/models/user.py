from flask_app.config.mysqlconnection import connectToMySQL

class User:

    def __init__(self, data):

        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL('users_schema').query_db(query)
    
        users = []
        
        for person in results:
            users.append(cls(person))
        return users
    @classmethod
    def save(cls,data):
        query = "INSERT INTO users(first_name, last_name ,email,created_at) VALUES (%(fname)s ,%(lname)s, %(email)s,NOW());"
        return connectToMySQL('users_schema').query_db( query, data )