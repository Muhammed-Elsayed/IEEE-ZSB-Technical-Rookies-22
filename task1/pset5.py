# pyhton
input1 = int(input("enter the number of elements in the list: "))
x = list(map(int, input("enter: ").split()))

# first using for loop
def adding_numbers_for(list):
   sum = 0
   for index in range(len(x)):
      sum += x[index]

   return sum


print(adding_numbers_for(x))


# second using while loop
def adding_numbers_while(list):
   sum = 0
   i = 0
   while len(list) > i:
      sum += x[i]
      i += 1
   return sum


print(adding_numbers_while(x))

# third using recursion
def adding_numbers_recursion(list):

      if len(list) == 0:
         return 0
      else:
         return list[0] + adding_numbers_recursion(list[1:])


print(adding_numbers_recursion(x))
