import random
secret_number = random.randint(1, 10)
print(secret_number)
counter = 0
while True:
    guess = int(input("enter your guess ? "))
    if guess == secret_number:
        counter += 1
        break
    else:
        print("wrong answer")
        counter += 1

print(f"Yay you got it {counter} tries ")
