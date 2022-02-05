def chocolateFeast(n, c, m):
    number_of_chocolates = n / c
    number_of_wrappers = number_of_chocolates
    while number_of_wrappers >= m:
        number_of_new_chocolates = number_of_wrappers // m
        number_of_chocolates += number_of_new_chocolates


        number_of_wrappers = (number_of_wrappers % m) + number_of_new_chocolates



    return int(number_of_chocolates)
