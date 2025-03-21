from flask import Flask, render_template, request, redirect, url_for, flash
import database

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
        identifier = request.form['identifier']  # This will be either username or email
        password = request.form['password']
        
        # Call the login function from database.py
        if database.login(identifier, password):
            flash('Login successful!', 'success')
            return redirect(url_for('dashboard'))  # Redirect to the dashboard after successful login
        else:
            flash('Incorrect username/email or password. Please try again.', 'danger')
    
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    return render_template('index.html')  # Render index.html after successful login

@app.route('/signup', methods=['GET', 'POST'])
def signup_page():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']  # Get email from the form
        password = request.form['password']
        confirm_password = request.form['confirm_password']
        
        # Check if the email is valid
        if not database.is_valid_email(email):
            flash('Invalid email address. Please enter a valid email.', 'danger')
            return redirect(url_for('signup_page'))
        
        # Check if passwords match
        if password != confirm_password:
            flash('Passwords do not match. Please try again.', 'danger')
            return redirect(url_for('signup_page'))

        # Call the signup function from database.py
        if database.signup(username, email, password):
            flash('Signup successful! You can now log in.', 'success')
            return redirect(url_for('login_page'))  # Redirect to login page after signup
        else:
            flash('Username or email already exists, please choose a different one.', 'danger')
    
    return render_template('signup.html')

if __name__ == '__main__':
    app.run(debug=True)
