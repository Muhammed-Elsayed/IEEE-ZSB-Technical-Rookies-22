def sockMerchant(n, ar):
    dic1 = {}
    counter1 = 0
    for num in ar:
        if num not in dic1:
            dic1[num] = 1
        else:
            dic1[num] += 1

    for x in dic1.values():
        while x >= 2:
            counter1 += 1
            x = x - 2

    return counter1
