from flask_app.config.mysqlconnection import connectToMySQL,DB

class Like:
    def __init__(self,data):
        self.id = data['id']
        self.user_id = data['user_id']
        self.show_id = data['show_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def create_like(cls,data):
        query = "INSERT INTO likes (user_id, show_id) VALUES (%(user_id)s, %(show_id)s);"
        return connectToMySQL(DB).query_db(query,data)
    
    @classmethod
    def delete_like(cls,data):
        query = "DELETE FROM likes WHERE user_id = %(user_id)s AND show_id = %(show_id)s;"
        return connectToMySQL(DB).query_db(query,data)
    
    @classmethod
    def get_likes_count(cls,data):
        query = "SELECT  COUNT(*) FROM likes WHERE  show_id = %(show_id)s;"
        result = connectToMySQL(DB).query_db(query,data)
        return result[0]['COUNT(*)']
    
    @classmethod
    def get_all_likes(cls):
        query = "SELECT * FROM likes;"
        results = connectToMySQL(DB).query_db(query)
        likes = []
        for row in results:
            likes.append( cls(row))
        return likes
    

    
    @classmethod
    def does_user_like_show(cls,data):
        query = "SELECT * FROM likes WHERE user_id = %(id)s ;"
        result = connectToMySQL(DB).query_db(query,data)
        results = []
        for row in result:
            results.append( cls(row))

        likes_list = results
        for like_obj in likes_list:
            print(like_obj.show_id)
        liked_shows = []
        for like_obj in likes_list:
            liked_shows.append(like_obj.show_id)
        print(liked_shows)
        
        
        return liked_shows


