from mysqlconnection import connectToMySQL
from ninja import Ninja

class Dojo:

    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

        self.ninjas = []

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query)
    
        dojos = []
    
        for dojo in results:
            dojos.append(cls(dojo))
        return dojos
    
    @classmethod
    def save(cls,data):

        query = "INSERT INTO dojos (name,created_at, updated_at) VALUES ( %(name)s,NOW(),NOW());"

        return connectToMySQL('dojos_and_ninjas_schema').query_db( query, data )
    
    @classmethod
    def get_dojos_with_ninjas(cls,data):


        query = "SELECT * FROM dojos LEFT JOIN ninjas ON ninjas.dojo_id = dojos.id WHERE dojo_id = %(id)s;"
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query,data)

        if results:

            ninjas = []
            dojo_ninja = cls(results[0])
            

            for row in results:
                ninja_data = {
                        "id" : row["ninjas.id"],
                        "fname" : row["first_name"],
                        "lname" : row["last_name"],
                        "age" : row["age"],
                        "created_at" : row["ninjas.created_at"],
                        "updated_at" : row["ninjas.updated_at"],
                        "dojo_id" : row["dojo_id"]
                        
                    }

                ninja = Ninja(ninja_data) 

            

                ninjas.append(ninja)
                dojo_ninja.ninjas = ninjas

        return dojo_ninja