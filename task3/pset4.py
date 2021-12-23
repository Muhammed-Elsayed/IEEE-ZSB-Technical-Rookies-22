# considering that x1 will be always in the back of x2
def kangaroo(x1, v1, x2, v2):

    if v1 > v2:
        if (x2 - x1) % (v2 - v1) == 0:
           return ("YES")

    return ("NO")

print(kangaroo(0, 3 , 4, 2))
