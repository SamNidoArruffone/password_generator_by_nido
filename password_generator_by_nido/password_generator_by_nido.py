import random
import string

def generate_password(length=12, use_uppercase=True, use_numbers=True, use_special=True):
    characters = string.ascii_lowercase
    
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_numbers:
        characters += string.digits
    if use_special:
        characters += "!@#$%^&*"
    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def save_password(password, filename="passwords_generated.txt"):
    with open(filename, "a") as file:  # "a" = append mode (keeps old passwords)
        file.write(password + "\n")

# User input
length = int(input("Enter password length: "))
uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
numbers = input("Include numbers? (y/n): ").lower() == 'y'
special = input("Include special characters? (y/n): ").lower() == 'y'

# Generate password
password = generate_password(length, uppercase, numbers, special)
print("Generated Password:", password)

# Save to file
save_password(password)
print(f"Password saved to 'passwords_generated.txt'")