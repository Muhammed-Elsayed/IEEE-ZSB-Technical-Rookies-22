#python

# getting the list and sort it first
mylist = list(map(int, input("please enter the list: ").split()))
mylist.sort()

# removing duplicates by using dictionary
def remove_duplicates(list):
    dict1 = {}
    new_list = []
    for index in list:
      if index not in dict1:
          dict1[index] = 1
          new_list.append(index)

    print(*new_list)


print(remove_duplicates(mylist))
