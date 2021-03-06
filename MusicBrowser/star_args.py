# def print_backwards(*args, **kwargs):
# def print_backwards(*args, **kwargs):
#     print(kwargs)
#     kwargs.pop('end', None)
#     print(kwargs)
#     for word in args[::-1]:
#         print(word[::-1], end=' ', **kwargs)
def print_backwards(*args, end=' ', **kwargs):
    end_character = kwargs.get('end', '\n')
    sep_character = kwargs.get('sep', '\n')
    for word in args[:0:-1]:
        print(word[::-1], end=sep_character, **kwargs)
    # print(end=end_character)
    print(args[0][::-1], end=end_character)


def backwards_print(*args, **kwargs):
    sep_character = kwargs.pop('sep', ' ')
    print(sep_character.join(word[::-1] for word in args[::-1]), **kwargs)


with open("backwards.txt", "w") as backwards:
    print_backwards("hello", "planet", "earth", "take", "me", "to", "your", "leader", end='\n')
    print("Another String")

print()
# print("hello", "planet", "earth", "take", "me", "to", "your", "leader", end='', sep='\n**\n')
# print_backwards("hello", "planet", "earth", "take", "me", "to", "your", "leader", end='', sep='\n**\n')
print("=" * 10)
backwards_print("1233453654765876879")
