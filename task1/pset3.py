#python
list1 = [1, 2, 3, 4, 5, 6, 7]


def binary_search(list, wanted_number):
    low = 0
    high = len(list1) - 1

    while high >= low:
        mid = (low + high) // 2

        if wanted_number == list1[mid]:
            return mid

        elif wanted_number > list1[mid]:
            low = mid + 1

        elif wanted_number < list1[mid]:
            high = mid - 1


print(binary_search(list1, 5))
