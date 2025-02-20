from db.connection import get_database_connection

class Post:
    def __init__(self, author_id, title, category, content):
        self.author_id = author_id
        self.title = title
        self.category = category
        self.content = content
    
    def save(self):
        conn = get_database_connection()
        if not conn:
            return False
        
        cursor = conn.cursor()
        try:
            cursor.execute(
                'INSERT INTO posts (title, content, author_id, category) VALUES(%s, %s, %s, %s)',
                (self.title, self.content, self.author_id, self.category)
            )
            conn.commit()
            return True
        except Exception as e:
            print(e)
            return False
        finally:
            cursor.close()
            conn.close()
    
    def get_posts():
        conn = get_database_connection()
        if not conn:
            return
        
        cursor = conn.cursor()
        try:
            cursor.execute('SELECT id, title, category, created_at FROM posts')
            posts = cursor.fetchall()
            return posts
        except Exception as e:
            print(e)
        finally:
            cursor.close()
            conn.close()