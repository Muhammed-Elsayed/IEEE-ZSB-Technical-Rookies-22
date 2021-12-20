#python
def is_a_palindrome(word):
    if word == word[::-1]:
       return True

    else:
        return False

word_given = input(" please enter a word : ")
print(is_a_palindrome(word_given))
