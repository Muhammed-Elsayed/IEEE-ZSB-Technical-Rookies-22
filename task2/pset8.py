if __name__ == '__main__':
    #to remove duplicates from a list
    from collections import OrderedDict

    python_students = []
    for index in range(int(input())):
        name = input()
        score = float(input())
        list1 = (name, score)
        python_students.append(list1)
    # for scores
    list1 = []
    # for names
    list2 = []

    for index in range(len(python_students)):
        list1.append(python_students[index][1])
    list1.sort()

    x = list(OrderedDict.fromkeys(list1))

    for n in range(len(python_students)):
        if python_students[n][1] == x[1]:
             list2.append(python_students[n][0])
    list2.sort()
    for z in list2:
        print(z)
