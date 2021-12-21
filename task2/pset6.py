n = int(input())
    list1 = list(map(int, input().split()))
    x = sorted(set(list1))
    print(x[-2])
 
