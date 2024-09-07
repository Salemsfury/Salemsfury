from flask import Flask, render_template, request
import re

app = Flask(__name__)

def check_password(password):
    # Define criteria
    min_length = 8
    has_uppercase = re.compile(r'[A-Z]')
    has_lowercase = re.compile(r'[a-z]')
    has_digit = re.compile(r'\d')
    has_special = re.compile(r'[!@#$%^&*(),.?":{}|<>]')
    
    # Check password length
    if len(password) < min_length:
        return "Password is too short. It must be at least 8 characters long."
    
    # Check for uppercase letter
    if not has_uppercase.search(password):
        return "Password must contain at least one uppercase letter."
    
    # Check for lowercase letter
    if not has_lowercase.search(password):
        return "Password must contain at least one lowercase letter."
    
    # Check for digit
    if not has_digit.search(password):
        return "Password must contain at least one digit."
    
    # Check for special character
    if not has_special.search(password):
        return "Password must contain at least one special character."
    
    # If all criteria are met
    return "Password is strong."

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        password = request.form['password']
        result = check_password(password)
        return render_template('result.html', result=result, password=password)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
