import copy
def getTotalX(a, b):
    def is_divided1(number):
        for index in a:
            if number % index != 0:
                return False

        return True

    list3 = []
    new_list = copy.deepcopy(list3)
    for index in range(1, min(b) + 1):
        if is_divided1(index) == True:
            list3.append(index)
    new_list = copy.deepcopy(list3)
    print(list3)
    for x in b:
        for index in range(len(list3)):
            if x % list3[index] != 0:
                if list3[index] in new_list:
                    new_list.remove(list3[index])

    print(new_list)
    return len(new_list)
