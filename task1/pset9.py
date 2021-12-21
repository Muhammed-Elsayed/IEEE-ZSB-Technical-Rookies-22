# fibonacci
number = int(input("please enter a number: "))
n1, n2 = 0, 1
if number <= 0:
    print("please enter a positive number")

elif number == 1:
    print(n1)

else:

    for index in range(number):
       print(n1)
       sum = n1 + n2
       n1 = n2
       n2 = sum


