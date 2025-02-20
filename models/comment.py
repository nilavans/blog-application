from db.connection import get_database_connection

class Comment:
    def __init__(self, post_id, user_id, comment):
        self.post_id = post_id
        self.user_id = user_id
        self.comment = comment

    def save(self):
        conn = get_database_connection()
        if not conn:
            return False
        
        cursor = conn.cursor()
        try:
            cursor.execute(
                'INSERT INTO comments (post_id, user_id, content) VALUES(%s, %s, %s)',
                (self.post_id, self.user_id, self.comment)
            )
            conn.commit()
            return True
        except Exception as e:
            print(e)
            return False
        finally:
            cursor.close()
            conn.close()