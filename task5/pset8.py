first = input()
second = input()
d1 = {}
d2 = {}
operations = 0
for i in first:
    try:
        d1[i] += 1
    except:
        d1[i] = 1

for j in second:
    try:
        d2[j] += 1
    except:
        d2[j] = 1

for k, v in d2.items():
   if k not in d1.keys():
       operations += v

   elif d1[k] != v:
       operations += abs(d1[k] - v)

for k, v in d1.items():
    if k not in d2.keys():
        operations += 1

print(operations)
