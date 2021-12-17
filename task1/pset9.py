# python
n = int(input("number: "))
list1 = [0, 1]
i = 0
for n in range(n - 2):
    number = list1[i] + list1[i + 1]
    list1.append(number)
    i += 1

print(list1)
