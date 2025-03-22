# app.py
from flask import Flask, render_template, redirect, url_for, flash
import database
from login_signup import auth_blueprint  # Import the auth blueprint

app = Flask(__name__)

# Secret key for session management
app.secret_key = 'your_secret_key_here'

# Create the database when the app starts
database.create_db()

# Register the blueprint for login and signup routes
app.register_blueprint(auth_blueprint, url_prefix='/auth')  # Prefix the routes with /auth

# Default route to redirect to the login page
@app.route('/')
def home():
    return redirect(url_for('auth.login_page'))  # Redirect to login page by default

@app.route('/dashboard')
def dashboard():
    return render_template('index.html')  # Render index.html after successful login

if __name__ == '__main__':
    app.run(debug=True)
