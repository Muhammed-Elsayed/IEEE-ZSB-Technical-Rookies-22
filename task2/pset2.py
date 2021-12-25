#python

# getting the list and sort it first
mylist = list(map(int, input("please enter the list: ").split(" ")))
mylist.sort()


def remove_duplicates(list):
    new_list = []
    for index in list:
      if index not in new_list:
          new_list.append(index)

    print(*new_list)


print(remove_duplicates(mylist))
