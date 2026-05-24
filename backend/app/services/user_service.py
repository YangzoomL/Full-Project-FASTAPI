from app.db.connection import get_connection
from app.schemas.user import UserCreate

def create_user(user: UserCreate) -> dict:
    conn = get_connection() #open a connection to the database

    try:
        with conn.cursor() as cur:

            cur.execute(
                "INSERT INTO users (email, name, age) VALUES (%s, %s, %s) RETURNING id",
                (user.email, user.name, user.age)
            )
            user_id = cur.fetchone()[0] #fetchone() returns a tuple, we want the first element which is the id of the newly created user
            conn.commit()
            return {"id": user_id, "name": user.name, "email": user.email, "age": user.age}
        
    finally:
        conn.close() 

def get_user() -> list:
    conn = get_connection() #open a connection to the database

    try:
        with conn.cursor() as cur:

            cur.execute("SELECT id, email, name, age FROM users")
            users = cur.fetchall() #fetchall() returns a list of tuples, we want to convert it to a list of dictionaries
            return [{"id": user[0], "email": user[1], "name": user[2], "age": user[3]} for user in users]
        
    finally:
        conn.close()

def find_user(user_id: int) -> dict | None :
    conn = get_connection() #open a connection to the database

    try:
        with conn.cursor() as cur:

            cur.execute("SELECT id, email, name, age FROM users WHERE id = %s", (user_id,))
            user = cur.fetchone() #fetchone() returns a tuple, we want to convert it to a dictionary
            if user is None:
                return None #raise an exception if the user is not found
            return {"id": user[0], "email": user[1], "name": user[2], "age": user[3]}
    
        
    finally:
        conn.close()



