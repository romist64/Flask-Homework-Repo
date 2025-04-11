from flask import Flask, render_template, request
import hashlib
import sqlite3
app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/signuplogin')
def hello():
    # Connect to database
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    
    # Create users table if it doesn't exist
    cursor.execute('''CREATE TABLE IF NOT EXISTS users 
                     (username TEXT PRIMARY KEY, password TEXT)''')
    conn.commit()
    
    # Show login form
    return render_template('login.html')

@app.route('/register', methods=['POST'])
def register():
    username = request.form['username'].lower()
    password = request.form['password']
    
    # Hash the password using SHA-256
    hashed = hashlib.sha256(password.encode()).hexdigest()
    
    try:
        # Insert new user
        cursor = sqlite3.connect('users.db').cursor()
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", 
                      (username, hashed))
        cursor.connection.commit()
        return "Registration successful!"
    except sqlite3.IntegrityError:
        return "Username already exists!"

@app.route('/login', methods=['POST']) 
def login():
    username = request.form['username'].lower()
    password = request.form['password']
    
    # Hash the entered password
    hashed = hashlib.sha256(password.encode()).hexdigest()
    
    # Check credentials
    cursor = sqlite3.connect('users.db').cursor()
    cursor.execute("SELECT password FROM users WHERE username = ?", (username,))
    result = cursor.fetchone()
    
    if result and result[0] == hashed:
        return "Login successful!"
    else:
        return "Invalid credentials!"

if __name__ == '__main__':
   app.run()