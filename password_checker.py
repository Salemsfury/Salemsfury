import re

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
    
if __name__ == "__main__":
    # List of test passwords
    test_passwords = [
        "12345678",            # Weak password (no special characters or uppercase)
        "Password1",           # Strong password (meets all criteria)
        "P@ssw0rd",            # Strong password (meets all criteria)
        "short",               # Weak password (too short)
        "NoDigitsOrSpecials"   # Weak password (no digits or special characters)
    ]

    # Test each password and print the result
    for pwd in test_passwords:
        print(f"Testing: {pwd}")
        print(check_password(pwd))
        print()
