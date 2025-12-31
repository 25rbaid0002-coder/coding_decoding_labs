import random
import string

# Function to generate password
def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ""
    for i in range(length):
        password += random.choice(characters)
    return password

# Function to validate password
def validate_password(password):
    length_check = len(password) >= 8
    upper_check = any(c.isupper() for c in password)
    lower_check = any(c.islower() for c in password)
    digit_check = any(c.isdigit() for c in password)
    # special_check = any(c in string.punctuation for c in password)

    score = length_check + upper_check + lower_check + digit_check  
    # special_check

    if score <= 2:
        return "Weak Password"
    elif score == 3 or score == 4:
        return "Medium Password"
    else:
        return "Strong Password"

# Main program
print("Password Generator and Validator")

choice = int(input("Enter 1 to Generate Password, 2 to Validate Password: "))

if choice == 1:
    length = int(input("Enter password length: "))
    new_password = generate_password(length)
    print("Generated Password:", new_password)

elif choice == 2:
    user_password = input("Enter password to validate: ")
    result = validate_password(user_password)
    print("Password Strength:", result)

else:
    print("Invalid choice")