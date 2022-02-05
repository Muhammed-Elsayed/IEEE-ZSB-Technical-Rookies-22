letter = "rar"
num = 10
def counting_the_letters(letter, num):
    while True:
        if len(letter) == num:
            break

        elif len(letter) > num:
            letter = letter[:-1]

        else:
            letter = letter + letter
    counter = 0
    for x in letter:
        if x == "r":
           counter += 1

    return counter


print(counting_the_letters(letter, num))
