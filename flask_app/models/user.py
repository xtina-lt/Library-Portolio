from flask_app.config.mysqlconnection import connectToMySQL
# import the following function
# def connectToMySQL(db):
#     return MySQLConnection(db)
# this is in flask app > config> mysqlconnection.py

class User:
    db = 'users_schema'

    def __init__(self, data):
        self.id = data["id"]
        self.name = data['name']
        self.email = data["email"]
        self.password = data["password"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
    
    '''READ'''
    @classmethod
    def select_all(cls):
        query = "SELECT id, CONCAT_WS(', ', last_name, first_name) AS name, email, password, created_at, updated_at FROM users"
        results = connectToMySQL(cls.db).query_db(query)
        return[cls(i) for i in results]
    
    @classmethod
    def get_one(cls,data):
        query  = "SELECT * FROM users WHERE id = %(id)s";
        result = connectToMySQL(cls.db).query_db(query,data)
        return result[0]
        # RETURNS THE DATA
        # shouldn't use class becuase our class consists of manipulated results
        # would be invalid
        # {'id': 1, 'first_name': 'Saint', 'last_name': 'Pattys', 'email': 'luckoirish@clover.com', 'password': 'password', 'created_at': dateti
    
    '''CREATE'''
    @classmethod
    def insert(cls, data):
        query = "INSERT INTO users ( first_name , last_name , email, password ) VALUES (%(first_name)s , %(last_name)s , %(email)s, %(password)s );"
        return connectToMySQL(cls.db).query_db( query, data )
        # RETURNS ID NUMBER

    '''UPDATE'''
    @classmethod
    def update(cls, data):
        query="UPDATE users SET first_name=%(first_name)s, last_name=%(last_name)s, email=%(email)s, password=%(password)s WHERE id=%(id)s"
        return connectToMySQL(cls.db).query_db(query,data)

    '''DELETE'''
    @classmethod
    def delete(cls,data):
        query = "DELETE FROM users_schema.users WHERE id=%(id)s"
        return connectToMySQL(cls.db).query_db(query,data)