import psycopg2
from .config import load_config

def get_database_connection():
    config = load_config()
    try:
        with psycopg2.connect(**config) as conn:
            print('Connected to PosgresSQL server..')
            return conn
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)

def create_tables():
    conn = get_database_connection()
    cursor = conn.cursor()
    try:
        with open('db/schema.sql', 'r') as schema:
            cursor.execute(schema.read())
        conn.commit()
        print('Schema executed successfully..')
    except Exception:
        print(Exception)
    finally:
        cursor.close()
        conn.close()
