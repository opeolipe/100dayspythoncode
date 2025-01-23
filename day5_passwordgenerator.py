import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))


# Easy Level 1
total_letters = len(letters)
total_numbers = len(numbers)
total_symbols = len(symbols)
password = ""

for i in range(nr_letters):
    random_letters = int(random.randint(0,total_letters-1))
    password += letters[random_letters]

for i in range(nr_numbers):
    random_number = int(random.randint(0,total_numbers-1))
    password += numbers[random_number]


for i in range(nr_symbols):
    random_symbols= int(random.randint(0,total_symbols-1))
    password += symbols[random_symbols]

print(password)


# Easy level 2
password = ""
for _ in range (nr_letters):
    password += random.choice(letters)

for _ in range (nr_numbers):
    password += random.choice(numbers)

for _ in range (nr_symbols) :
    password += random.choice(symbols)

print(password)

# Hard one

password_list=list(password)
random.shuffle(password_list)
password_final = ''.join(password_list)
print(password_final)

# Hard one 2

password_list = []
for char in range (0, nr_letters):
    password_list.append(random.choice(letters))

for char in range (0, nr_symbols):
    password_list.append(random.choice(symbols))

for char in range (0, nr_numbers):
    password_list.append(random.choice(numbers))

print(password_list)
random.shuffle(password_list)
print(password_list)

password = ""
for char in password_list:
    password += char

print(f"Your password is:{password}")



