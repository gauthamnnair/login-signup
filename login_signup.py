from flask import Flask, render_template, request, redirect, url_for, flash
import database  # Import functions from database.py

app = Flask(__name__)

# Secret key for session management
app.secret_key = 'your_secret_key_here'

# Create the database when the app starts
database.create_db()

# Default route to redirect to the login page
@app.route('/')
def home():
    return redirect(url_for('login_page'))  # Redirect to login page by default

@app.route('/login', methods=['GET', 'POST'])
def login_page():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # Call the login function from database.py
        if database.login(username, password):
            flash('Login successful!', 'success')
            return redirect(url_for('dashboard'))  # Redirect to the dashboard after successful login
        else:
            flash('Incorrect username or password. Please try again.', 'danger')
    
    return render_template('login.html')

# Change 'index' to 'dashboard' to avoid conflict
@app.route('/dashboard')
def dashboard():
    return render_template('index.html')  # Render index.html after successful login

@app.route('/signup', methods=['GET', 'POST'])
def signup_page():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # Call the signup function from database.py
        if database.signup(username, password):
            flash('Signup successful! You can now log in.', 'success')
            return redirect(url_for('login_page'))  # Redirect to login page after signup
        else:
            flash('Username already exists, please choose a different one.', 'danger')
    
    return render_template('signup.html')

if __name__ == '__main__':
    app.run(debug=True)
