def findDigits(n):
    counter = 0
    list1 = list(map(int, str(n)))
    for number in list1:
       try:
          if n % number == 0:
             counter += 1
       except:
           pass

    return counter



print(findDigits(1012))
