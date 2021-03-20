import random


def guess_integer(prompt):
    while True:
        temp = input(prompt)
        if temp.isnumeric():
            return int(temp)
        else:
            print("{0} is not a valid number.".format(temp))


highest = 1000
answer = random.randint(1, highest)
# print(answer)    # TODO: Remove after testing
guess = 0   # initialise to any number that doesn't equal to the answer
print("Please guess a number between 1 and {}: ".format(highest))

while guess != answer:
    guess = guess_integer(": ")

    if guess == answer:
        print("Well done, you guessed it")
        break
    else:
        if guess < answer:
            print("Please guess higher")
        else:   # guess must be higher than answer
            print("Please guess lower")

        if guess == 0:
            print("Bye bye")
            break
