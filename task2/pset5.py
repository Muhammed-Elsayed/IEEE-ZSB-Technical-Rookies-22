list1 = [8, 2, 4, 1, 3]

def insertion_sort(list):
    for i in range(1, len(list1)):
        key = list[i]
        j = i - 1
        while list[j] > key and j >= 0:
            list[j + 1 ] = list[j]
            j -= 1
        list[j + 1] = key

    return list



print(insertion_sort(list1))
