import random
import string

print("Welcome to the password generator")
password_length = int(input("Enter password length: "))

characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")
#random.shuffle(characters)

password = []
for i in range(password_length):
	password.append(random.choice(characters))

print("".join(password))



