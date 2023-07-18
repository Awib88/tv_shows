from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL,DB
from flask import flash
from datetime import datetime

class Show:
    def __init__(self,data):
        self.id = data['id']
        self.user_id = data['user_id']
        self.title = data['title']
        self.network = data['network']
        self.release_date = data['release_date']
        self.type = data['type']
        self.age_limit = data['age_limit']
        self.description = data['description']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        #---------------------------------------------------
    
    
    @classmethod
    def save(cls,data):
        query = "INSERT INTO shows (user_id,title,network,release_date,type,age_limit,description) VALUES (%(user_id)s,%(title)s,%(network)s,%(release_date)s,%(type)s,%(age_limit)s,%(description)s);"
        return connectToMySQL(DB).query_db(query,data)
    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM shows;"
        results = connectToMySQL(DB).query_db(query)
        shows = []
        for row in results:
            shows.append( cls(row))
        return shows
    
    @classmethod
    def get_one(cls,data):
        query = "SELECT * FROM shows WHERE id = %(id)s;"
        results = connectToMySQL(DB).query_db(query,data)
        return cls(results[0])
    
    @classmethod
    def update(cls,data):
        query = "UPDATE shows SET title=%(title)s,network=%(network)s,release_date=%(release_date)s, type=%(type)s,age_limit=%(age_limit)s,description=%(description)s WHERE id=%(id)s;"
        return connectToMySQL(DB).query_db(query,data)
    
    @classmethod
    def delete(cls,data):
        query = "DELETE FROM shows WHERE id=%(id)s;"
        return connectToMySQL(DB).query_db(query,data)
    
    @classmethod
    def get_all_by_user_id(cls,data):
        query = "SELECT * FROM shows WHERE user_id = %(id)s;"
        results = connectToMySQL(DB).query_db(query,data)
        shows = []
        for row in results:
            shows.append( cls(row))
        return shows
    
    @classmethod
    def get_all_by_date(cls):
        query = "SELECT * FROM shows ORDER BY release_date DESC;"
        results = connectToMySQL(DB).query_db(query)
        shows = []
        for row in results:
            shows.append( cls(row))
        return shows
    
    
    
    @classmethod
    def count_all(cls):
        query = "SELECT COUNT(*) FROM shows;"
        result= connectToMySQL(DB).query_db(query)
        return result[0]['COUNT(*)']
    
    
#----------------------------show validation-----------------------------------------
    @staticmethod
    def validate_show(data):
        is_valid = True
        if len(data['title']) < 3:
            flash("Title Must be at least 3 characters long!",'show')
            is_valid=False
        if len(data['network']) < 3:
            flash("Network Must be at least 3 characters long!",'show')
            is_valid=False
        if len(data['description']) < 10:
            flash("Description Must be at least 10 characters long!",'show')
            is_valid=False
        if data['release_date'] > str(datetime.now()):
            flash("Release Date :Unless you can travel to future please correct the date!",'show')
            is_valid=False
        return is_valid