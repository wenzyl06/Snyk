import sqlite3

def authenticate(username, password):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    
    # Vulnerability 1: SQL Injection
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    cursor.execute(query)
    result = cursor.fetchone()
    
    if result:
        print("Login successful!")
    else:
        print("Login failed!")
        
    conn.close()

# Vulnerability 2: Hardcoded credentials
admin_password = "supersecret123"

def get_file(filename):
    # Vulnerability 3: Path traversal
    with open("/home/data/" + filename, "r") as f:
        print(f.read())

# Vulnerability 4: Insecure random numbers
import random
token = str(random.randint(100000, 999999))
print("Auth Token:", token)

username = input("Username: ")
password = input("Password: ")
authenticate(username, password)

filename = input("Enter filename: ")
get_file(filename)