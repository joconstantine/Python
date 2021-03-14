print("Please choose your option from the list below:")
print("1. Learn Python")
print("2. Learn Java")
print("3. Go swimming")
print("4. Have dinner")
print("5. Go to bed")
print("0. Exit")

choice = ""

while choice != 0:
    choice = int(input())
    if choice == 0:
        print("Bye Bye")
    elif 1 <= choice <= 6:
        print("You have chosen option {}".format(choice))
    else:
        print("You have chosen a wrong option")
        print("Please choose your option from the list below:")
        print("1. Learn Python")
        print("2. Learn Java")
        print("3. Go swimming")
        print("4. Have dinner")
        print("5. Go to bed")
        print("0. Exit")

