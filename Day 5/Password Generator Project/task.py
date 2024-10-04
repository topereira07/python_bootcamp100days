import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# easy level
password = ""

for letter in range(0,nr_letters):
    password += random.choice(letters)
for number in range(0,nr_numbers):
    password += random.choice(numbers)
for number in range(0,nr_symbols):
    password += random.choice(symbols)

print(password)

# hard level - my implementation
shuffled_password = list(password)
random.shuffle(shuffled_password)
result =''.join(shuffled_password)
print(result)

# hard level - angela implementation

new_password = []
new_shuffled_password = ""
for letter in range(0,nr_letters):
    new_password.append(random.choice(letters))
for number in range(0,nr_numbers):
    new_password.append(random.choice(numbers))
for number in range(0,nr_symbols):
    new_password.append(random.choice(symbols))

random.shuffle(new_password)

for char in new_password:
    new_shuffled_password += char

print (new_shuffled_password)


