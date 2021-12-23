def breakingRecords(scores):
    min_count = 0
    max_count = 0
    highest_score = scores[0]
    lowest_score = scores[0]


    for n in scores:
        print("mo")
        if n < lowest_score:
            lowest_score = n
            min_count += 1
            print(min_count)
        elif n > highest_score:
            
            highest_score = n

            max_count += 1
            print(max_count)


    list1 = [max_count, min_count]
    return list1
