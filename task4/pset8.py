def stones(n, a, b):
   if a > b:
       a, b = b, a
   list1 = []
   x = b * (n - 1)
   for i in range(n):
       list1.append(x)
       if a == b:
           break
       x = x - b + a
   list1.sort()
   return list1
