

def countingValleys(steps, path):
    counter = 0
    current_position = 0

    for letter in path:
        if letter == "D":
            current_position -= 1

        elif letter == "U":
            current_position += 1

        if current_position == 0 and letter == "U":
            counter += 1
    
    return counter
