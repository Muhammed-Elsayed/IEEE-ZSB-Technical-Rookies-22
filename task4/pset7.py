def kaprekarNumbers(p, q):
    lst = []

    for index in range(p, q + 1):
        if index == 1:
            lst.append(index)

        if index > 8:
            square_number = index * index
            square_number_str = str(square_number)
            first_part = square_number_str[:len(square_number_str) // 2]

            second_part = square_number_str[len(square_number_str) // 2:]

            if int(first_part) + int(second_part) == index:
                     lst.append(index)

    for k in range(len(lst)):
        lst[k] = str(lst[k])
    if len(lst) == 0:
        return ("INVALID RANGE")

    return " ".join(lst)
