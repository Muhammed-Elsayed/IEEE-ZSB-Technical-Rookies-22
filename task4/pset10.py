def getMoneySpent(keyboards, drives, b):
    keyboards.sort(reverse=True)
    drives.sort(reverse=True)
    sum = 0
    max_money_spent = 0

    for i in keyboards:
        for j in drives:
           sum = i + j
           if sum <= b and sum > max_money_spent:
               max_money_spent = sum

    if max_money_spent == 0:
        return -1
    return max_money_spent


b = 60
keyboards = [40, 50, 60]
drives = [5, 8, 12]

print(getMoneySpent(keyboards, drives, b))
