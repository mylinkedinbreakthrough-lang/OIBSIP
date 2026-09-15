import random
import string

password_length = int(input("Enter password length: "))

if password_length <= 0:
    print("Password length must be greater than zero.")
    exit()

characters = string.ascii_letters + string.digits + string.punctuation

password = ""

for i in range(password_length):
    character = random.choice(characters)
    password = password + character

print("Generated password:", password)
