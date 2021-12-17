# python
n = int(input("please enter a number: "))

def is_a_prime(n):
    for index in range(2, n):
        if n % index == 0:
            return False

    return True


def pset(n):
    list1 = []
    for index in range(2, n):
        if is_a_prime(index) == True:
            list1.append(index)


    print(*list1)


print(pset(n))

