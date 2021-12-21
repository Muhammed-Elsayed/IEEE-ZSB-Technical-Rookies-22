import random

secret_number = str(random.randint(100, 999))

while True:
    number_of_hits = 0
    number_of_misses = 0
    guess_number = input("enter the 3 digit  number: ")

    for index in range(3):
        if guess_number[index] in secret_number:
          
            if guess_number[index] == secret_number[index]:
                number_of_hits += 1

            else:
                number_of_misses += 1
    print(f" {number_of_hits} hits   {number_of_misses} misses")

    if guess_number == secret_number:
        break
