import sqlite3
import bcrypt

# Function to initialize the SQLite database and create the table if it doesn't exist
def create_db():
    conn = sqlite3.connect('user_database.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT NOT NULL UNIQUE,
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

# Function to sign up a new user (stores hashed password in the database)
def signup(username, password):
    hashed_password = hash_password(password)
    
    conn = sqlite3.connect('user_database.db')
    c = conn.cursor()
    
    try:
        c.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed_password))
        conn.commit()
        conn.close()
        return True
    except sqlite3.IntegrityError:
        conn.close()
        return False

# Function to login a user (checks the entered password with the stored hashed password)
def login(username, password):
    conn = sqlite3.connect('user_database.db')
    c = conn.cursor()
    c.execute("SELECT password FROM users WHERE username = ?", (username,))
    
    result = c.fetchone()
    conn.close()
    
    if result:
        stored_password = result[0]
        if verify_password(password, stored_password):
            return True
    return False
