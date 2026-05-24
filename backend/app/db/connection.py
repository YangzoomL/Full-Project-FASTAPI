import psycopg2 #postgreSQL database adapter for Python
import os #read environment variables

def get_connection():

    return psycopg2.connect(
        host = os.getenv("DB_HOST", "db"), #default value is "db" which is the name of the service in docker-compose.yml
        database = os.getenv("DB_NAME", "appdb"), #default value is "appdb" which is the name of the database in docker-compose.yml
        user = os.getenv("DB_USER", "postgres"), #default value is "appuser" which is the name of the user in docker-compose.yml
        password = os.getenv("DB_PASSWORD", "password") #default value is "password" which is the password of the user in docker-compose.yml
    )