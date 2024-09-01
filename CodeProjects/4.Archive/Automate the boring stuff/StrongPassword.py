import re

def is_strong_password(password):
    # Check if the password is at least 8 characters long
    if len(password) < 8:
        return False

    # Check if the password has both uppercase and lowercase characters
    if not re.search(r'[a-z]', password) or re.search(r'[A-Z]', password):
        return False

    # Check if password contains at least one digit
    if not re.search(r'[0-9]', password):
        return False

    # Check if password contain at least one character
    if not re.search(r'[˜!@#$%ˆ&*]', password):
        return False

    # If all conditions are met, the password is strong
    return True

# Example usage
password = input("Enter your pasword:")
if is_strong_password(password):
    print("Strong password! Good Job!")
else:
    print("Weak password. Please make sure your password is at least 8 characters long, contains both uppercase and lowercase characters, and has at least one digit.")


