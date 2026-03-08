import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


letters_count = int(input("how many letters do you want? : "))
numbers_count = int(input("how many numbers do you want? : "))
symbols_count = int(input("how many symbols do you want? : "))

password_members = []

for char in range(1, letters_count+1):
    password_members.append(random.choice(letters))

for char in range(1, numbers_count+1):
    password_members.append(random.choice(numbers))

for char in range(1, symbols_count+1):
    password_members.append(random.choice(symbols))

random.shuffle(password_members)

password = ""

for char in password_members:
    password += char

print(f"Your password is: {password}")
