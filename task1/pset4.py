# python
sentence = "hello world in a frame"

def max_length(sentence):
    max_lenth = 0
    word = ''
    for index in sentence.split():

        if len(index) > max_lenth:
            max_lenth = len(index)
            word = index

    return word

number_of_stars = "*" * (len(max_length(sentence)) + 4)
print(number_of_stars)
for index in sentence.split():
    length1 = len(max_length(sentence)) - len(index)
    print("*" + " " + index + " " + " " * length1 + "* " )

print(number_of_stars)
