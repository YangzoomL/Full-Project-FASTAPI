-- This SQL script initializes the database by creating a 'users' table if it doesn't already exist. The table includes an auto-incrementing 'id' as the primary key, a 'name' field for the user's name, an 'email' field that must be unique, and an 'age' field for the user's age.
CREATE TABLE IF NOT EXISTS users (
    id    SERIAL PRIMARY KEY,       
    name  VARCHAR(100) NOT NULL,     
    email VARCHAR(255) UNIQUE NOT NULL,  
    age   INTEGER                    
);