import string, random

L_letters = list(string.ascii_lowercase)
U_letters = list(string.ascii_uppercase)
numbers = list(string.digits)
symbols = list(string.punctuation)

print("Welcome to the PyPassword Generator!")
pass_upper = input("How many upper case letters would you like in your password? ")
pass_lower = input("How many Lower case letters would you like in your password? ")
pass_symbols = input("How many symbols would you like in your password? ")
pass_numbers = input("How many numbers would you like in your password? ")

password = []
for i in range(0, int(pass_upper)):
    password += random.choice(L_letters)
for i in range(0, int(pass_lower)):
    password += random.choice(U_letters)
for i in range(0, int(pass_symbols)):
    password += random.choice(symbols)
for i in range(0, int(pass_numbers)):
    password += random.choice(numbers)

final_password = []
for chr in range(0, len(password)):
    temp = random.choice(password)
    password.remove(temp)
    final_password.append(temp)

print("".join(final_password))