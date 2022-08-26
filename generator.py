import random
import string

uppercase = list(string.ascii_uppercase)
lowercase = list(string.ascii_lowercase)
digits = list(string.digits)
special_characters = list("!@#$%^&*()")
characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")

print("Welcome to the password generator")

while True:
    password_length = int(input("Enter password length (at least 4 characters): "))
    if password_length >= 4:
        break
    else:
        print("Incorrect length! Type again.")
        continue

password = [random.choice(uppercase), random.choice(lowercase), random.choice(digits), random.choice(special_characters)]

while len(password) < password_length:
    password.append(random.choice(characters))

random.shuffle(password)

print("Your password is " + "".join(password))



