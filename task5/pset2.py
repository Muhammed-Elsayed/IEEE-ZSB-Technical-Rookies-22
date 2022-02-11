n, t = input().split()
lst = list(map(int, input().split()))

time = 0
for item in range(len(lst)):
    time += 86400 - lst[item]
    if time >= int(t):
        print(item + 1)
        break
