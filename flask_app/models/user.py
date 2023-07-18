from flask_app.config.mysqlconnection import connectToMySQL,DB
from flask import flash
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
PW_REGEX= re.compile("^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$")

#----------------------------------------------------------
class User:
    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    #---------------------------------------------------

    @classmethod
    def save(cls,data):
        query = "INSERT INTO users (first_name,last_name,email,password) VALUES(%(first_name)s,%(last_name)s,%(email)s,%(password)s)"
        return connectToMySQL(DB).query_db(query,data)
    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL(DB).query_db(query)
        users = []
        for row in results:
            users.append( cls(row))
        return users
    
    @classmethod
    def get_by_email(cls,data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        results = connectToMySQL(DB).query_db(query,data)
        if (results) :
            return cls(results[0])
        return False
    
    @classmethod
    def get_by_id(cls,data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        results = connectToMySQL(DB).query_db(query,data)
        return cls(results[0])
    
    #----------------------------registration validation-----------------------------------------
    @staticmethod
    def validate_register(data):
        is_valid = True
        query= 'SELECT * FROM users WHERE email = %(email)s;'
        result= connectToMySQL(DB).query_db(query,data)
        if len(result) >= 1:
            flash("Email already exists",'register')
            is_valid= False
        if len(data['first_name']) < 3:
            flash("Firstname Must be at least 3 characters long!",'register')
            is_valid=False
        if len(data['last_name']) < 3:
            flash("Lastname Must be at least 3 characters long!",'register')
            is_valid=False
        if not EMAIL_REGEX.match(data['email']):
            flash("Invalid email",'register')
            is_valid=False
        if not PW_REGEX.match(data['password']):
            flash("Invalid password: Has minimum 8 characters in length+ At least one uppercase English letter +At least one lowercase English letter +At least one digit +At least one special character",'register')
            is_valid=False
        if data['password'] != data['confirm_password']:
            flash("Passwords don't match",'register')
        return is_valid



