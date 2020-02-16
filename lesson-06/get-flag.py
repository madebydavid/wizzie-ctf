#!/usr/bin/env ./../bin/python3

password_codes = [109, 97, 110, 99, 104, 101, 103, 111]

# https://docs.python.org/3/library/functions.html#ord
def get_letter_codes(thing_to_encode):
    codes = []
    for letter in thing_to_encode:
        codes.append(ord(letter))
    return codes

password = input('Please enter the password: ')
if get_letter_codes(password) == password_codes:
    with open('flag.txt', newline='') as f:
        print('The flag is: '+f.read(), end='')

