from db.connection import get_database_connection

class User:
    def __init__(self, username, email, password, role = 'reader'):
        self.username = username
        self.email = email
        self.password = password
        self.role = role
    
    def save(self):
        conn = get_database_connection()
        if not conn:
            return False
        
        cursor = conn.cursor()
        try:
            cursor.execute(
                'INSERT INTO users (username, email, password, role) VALUES(%s, %s, %s, %s)',
                (self.username, self.email, self.password, self.role)
            )
            conn.commit()
            return True
        except Exception as e:
            print(e)
            return False
        finally:
            cursor.close()
            conn.close()
    
    @staticmethod
    def authenticate(username, password):
        conn = get_database_connection()
        if not conn:
            return False
        
        cursor = conn.cursor()
        try:
            cursor.execute(
                'SELECT id, role FROM users WHERE username= %s AND password = %s',
                (username, password)
            )
            user = cursor.fetchone()
            return user if user else None
        except Exception as e:
            print(e)
            return False
        finally:
            cursor.close()
            conn.close()