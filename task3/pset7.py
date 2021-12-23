def migratoryBirds(arr):
    dict1 = {}
    list1 = []
    for num in arr:
         if num not in dict1.keys():
             dict1[num] = 1
         else:
             dict1[num] += 1

    max_value = max(dict1.values())
    for key in dict1.keys():
         if  dict1[key] == max_value:
             list1.append(key)
    list1.sort()

    return list1[0]
