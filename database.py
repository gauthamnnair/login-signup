import sqlite3
import bcrypt
import re

# Function to initialize the SQLite database and create the table if it doesn't exist
def create_db():
    conn = sqlite3.connect('user_database.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT NOT NULL UNIQUE,
                    email TEXT NOT NULL UNIQUE,
                    password TEXT NOT NULL)''')
    conn.commit()
    conn.close()

# Function to hash the password using bcrypt
def hash_password(password):
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password

# Function to verify the entered password with the stored hashed password
def verify_password(entered_password, stored_password):
    return bcrypt.checkpw(entered_password.encode('utf-8'), stored_password)

# Define the regex pattern for email validation
def is_valid_email(email):
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if re.match(email_regex, email):
        return True
    return False

# Function to sign up a new user (stores hashed password and username in the database)
def signup(username, email, password):
    hashed_password = hash_password(password)
    
    conn = sqlite3.connect('user_database.db')
    c = conn.cursor()
    
    try:
        c.execute("INSERT INTO users (username, email, password) VALUES (?, ?, ?)", (username, email, hashed_password))
        conn.commit()
        conn.close()
        return True
    except sqlite3.IntegrityError:
        conn.close()
        return False

# Function to login a user (checks the entered password with the stored hashed password)
def login(identifier, password):
    conn = sqlite3.connect('user_database.db')
    c = conn.cursor()
    
    # Check if the identifier is an email or username
    if '@' in identifier:  # It's likely an email
        c.execute("SELECT username, password FROM users WHERE email = ?", (identifier,))
    else:  # It's a username
        c.execute("SELECT username, password FROM users WHERE username = ?", (identifier,))
    
    result = c.fetchone()
    conn.close()
    
    if result:
        stored_username, stored_password = result
        if verify_password(password, stored_password):
            return True
    return False
