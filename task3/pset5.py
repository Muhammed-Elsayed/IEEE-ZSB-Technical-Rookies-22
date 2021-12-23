length_of_list = int(input("enter the length of the list: "))
scores = list(map(int, input("enter the elements of the list here: ").split()))

def breakingRecords(scores):
    min_count = 0
    max_count = 0
    highest_score = scores[0]
    lowest_score = scores[0]


    for n in scores:
        if n < lowest_score:
            lowest_score = n
            min_count += 1

        elif n > highest_score:
            highest_score = n
            max_count += 1

    return [max_count, min_count]

print(breakingRecords(scores))

