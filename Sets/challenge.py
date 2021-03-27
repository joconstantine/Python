# Create a program that takes some text and returns a list of
# all the characters in the text that are not vowels, sorted in
# alphabetical order.
#
# You can either enter the text from the keyboard or
# initialise a string variable with the string.

text = input("Please enter some text: ")
vowels = frozenset("aeiou")
text_set = set(text)
no_vowel = sorted(text_set.difference(vowels))
print(no_vowel)
