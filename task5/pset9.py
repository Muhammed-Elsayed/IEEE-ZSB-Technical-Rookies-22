def hackerrankInString(s):
    sub = "hackerrank"
    counter = 0

    for value in s:
        if value == sub[counter]:
            counter += 1
            if counter == len(sub):
                return 'YES'

    return 'NO'
