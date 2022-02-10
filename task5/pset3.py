def circularArrayRotation(a, k, queries):
    for index in range(k):
        a.insert(0, a[-1])
        a.pop()
    list1 = []
    for n in range(len(queries)):
        list1.append(a[queries[n]])

    return list1
