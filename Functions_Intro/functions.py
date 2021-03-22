def multiply(x: float, y: float) -> float:
    result = x * y
    # return result


def is_palindrome(string: str) -> bool:
    # backwards = string[::-1]
    # return backwards == string
    return string[::-1].casefold() == string.casefold()


def palindrome_sentence(sentence: str) -> bool:
    char_list = list(sentence)
    for index in range(len(char_list) - 1, -1, -1):
        if not char_list[index].isalnum():
            del char_list[index]

    return is_palindrome("".join(char_list))


# word = input("Please enter a word to check: ")
# if palindrome_sentence(word):
#     print("'{}' is a palindrome".format(word))
# else:
#     print("'{}' is not a palindrome".format(word))


def fibonacci(n):
    """Return the `n` th Fibonacci number, for positive `n`."""
    if 0 <= n <= 1:
        return n

    n_minus1, n_minus2 = 1, 0

    result = None
    for f in range(n - 1):
        result = n_minus2 + n_minus1
        n_minus2 = n_minus1
        n_minus1 = result

    return result


for i in range(36):
    print(i, fibonacci(i))

p = palindrome_sentence(242)
