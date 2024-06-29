from mysqlconnection import connectToMySQL


class Ninja:
    def __init__( self , db_data ):
        self.id = db_data['id']
        self.first_name = db_data['fname']
        self.last_name = db_data['lname']
        self.age = db_data['age']
        self.created_at = db_data['created_at']
        self.updated_at = db_data['updated_at']
        self.dojo_id = db_data['dojo_id']

    @classmethod
    def save( cls , data ):
        query = "INSERT INTO ninjas (first_name,last_name,age,created_at,updated_at,dojo_id) VALUES (%(fname)s, %(lname)s, %(age)s,NOW(),NOW(),%(dojo_id)s);"
        return connectToMySQL('dojos_and_ninjas_schema').query_db(query,data)
