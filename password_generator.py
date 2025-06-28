import random
import string

print("Password Generator")

length_str = input("Enter password length: ")

if length_str.isdigit():
    length = int(length_str)
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    print("Generated Password:", password)
else:
    print("Invalid input. Please enter a number.")
