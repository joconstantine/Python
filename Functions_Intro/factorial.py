def factorial(x: int) -> int:
    """
    This function computes the factorial of an integer
    :param x: input number
    :return: the factorial of the input number
    """
    if x < 0:
        raise ValueError("The input must be a positive integer")

    if x == 0:
        return 1
    else:
        return x * factorial(x - 1)


for index in range(36):
    print(index, factorial(index))
