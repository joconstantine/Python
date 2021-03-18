def multiply(x, y):
    result = x * y
    return result


def is_palindrome(string):
    # backwards = string[::-1]
    # return backwards == string
    return string[::-1].casefold() == string.casefold()


def palindrome_sentence(sentence):
    char_list = list(sentence)
    for index in range(len(char_list) - 1, -1, -1):
        if not char_list[index].isalnum():
            del char_list[index]

    return is_palindrome("".join(char_list))


word = input("Please enter a word to check: ")
if palindrome_sentence(word):
    print("'{}' is a palindrome".format(word))
else:
    print("'{}' is not a palindrome".format(word))
