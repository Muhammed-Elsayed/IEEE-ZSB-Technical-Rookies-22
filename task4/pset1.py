list1 = [2, 5, 3, 4, 1, 2]
list2 = []
list3 = []
list4 = []
for num in list1:
    if num not in list2:
        list2.append(num)
    else:
        list3.append(num)

for index in range(len(list1)):
    if list1[index] == list3[0]:
        list4.append(index)

print(list4[1] - list4[0])
