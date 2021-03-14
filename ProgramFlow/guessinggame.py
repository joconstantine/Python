import random

highest = 1000
answer = random.randint(1, highest)
# print(answer)    # TODO: Remove after testing
guess = 0   # initialise to any number that doesn't equal to the answer
print("Please guess a number between 1 and {}: ".format(highest))

count = 0
while guess != answer:
    guess = int(input())

    if guess == answer:
        print("Well done, you guessed it")
        break
    else:
        count += 1
        if guess < answer:
            print("Please guess higher")
        else:   # guess must be higher than answer
            print("Please guess lower")

        if guess == 0:
            print("Bye bye")
            break

        if count == 10:
            print("You guessed to many times")
            break
