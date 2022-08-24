import random
import string

uppercase = list(string.ascii_uppercase)
lowercase = list(string.ascii_lowercase)
digits = list(string.digits)
special_characters = list("!@#$%^&*()")
characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")
correct_length = False

print("Welcome to the password generator")
while correct_length == False:
    password_length = int(input("Enter password length (at least 4 characters): "))
    if password_length >= 4:
        correct_length = True
    else:
        print("Incorrect length! Type again.")

#random.shuffle(characters)

password = []
for i in range(password_length):
	password.append(random.choice(uppercase))

for i in range(password_length):
	password.append(random.choice(lowercase))

for i in range(password_length):
	password.append(random.choice(digits))

for i in range(password_length):
	password.append(random.choice(special_characters))

print("".join(password))



