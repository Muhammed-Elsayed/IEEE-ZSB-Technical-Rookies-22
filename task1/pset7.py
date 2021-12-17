# python
n = int(input("please enter a number: "))
sum = 0
for x in range(n + 1):
    if x % 3 == 0 or x % 5 == 0:
     sum += x

print(sum)
