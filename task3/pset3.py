import string
import random

letters = list(string.ascii_letters)
digits = list(string.digits)
special_letters = list("@#$%&")
my_password = []

for index in range(8):
    my_password.append(random.choice(letters))

my_password.append(random.choice(digits))
my_password.append(random.choice(special_letters))
random.shuffle(my_password)

print("".join(my_password))
