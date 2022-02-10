def beautifulTriplets(d, arr):
     triplets_numbers = 0
     for index in range(len(arr)):
         i = arr[index]
         j = i + d
         k = j + d
         if j in arr and k in arr:
             triplets_numbers += 1

     return triplets_numbers
