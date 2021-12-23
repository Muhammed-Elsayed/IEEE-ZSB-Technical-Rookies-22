def water_bottles():
    n = int(input("please enter a positive number : "))
    Total_remaining_volume = 0
    list1 = []
    for index in range(n):
        remaining_volume, capacity = map(int, input("enter two numbers: ").split())
        Total_remaining_volume += remaining_volume
        list1.append(capacity)

    list1.sort(reverse = True)

    if Total_remaining_volume > list1[0] + list1[1]:
        return ("no")
    else:
        return ("yes")

print(water_bottles())
