def libraryFine(d1, m1, y1, d2, m2, y2):
    if y2 == y1:
        if m2 == m1:
            if d2 >= d1:
                fine = 0

            else:
                number_of_days = d1 - d2
                fine = number_of_days * 15

        else:
            if m2 > m1:
                fine = 0
            else:
              number_of_months = m1 - m2
              fine = number_of_months * 500
    else:
        if y2 > y1:
            fine = 0
        else:
            fine = 10000
    return fine
