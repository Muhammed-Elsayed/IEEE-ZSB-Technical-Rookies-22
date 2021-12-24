# this fuction should take an input as integer and return a sorted integer in ascending order
number = int(input("please enter a number: "))
def ascending(number):

    number = str(number)
    if len(number) != 4:
        number = "0" + number
    number = list(number)
    number.sort()
    x = "".join(number)
    return int(x)

# this fuction should take an input as a integer and return a sorted integer in descending order
def descending(number):
    number = str(number)
    if len(number) != 4:
        number = "0" + number
    number = list(number)
    number.sort(reverse=True)
    x = "".join(number)
    return int(x)

n = 0
counter = -1
while True:

   result = descending(number) - ascending(number)
   counter += 1
   if number == result:
       break
   number = result



print(counter)

