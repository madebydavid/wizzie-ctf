#!/usr/bin/env ./../bin/python3

# Remember how the ord function works?
# https://docs.python.org/3/library/functions.html#ord
def get_total_value_of_letters(word):
    total = 0
    for letter in word:
        total += ord(letter)
    return total

password = input('Please enter the password: ')

if get_total_value_of_letters(password) == 528:
    with open('flag.txt', newline='') as f:
        print('The flag is: '+f.read(), end='')

