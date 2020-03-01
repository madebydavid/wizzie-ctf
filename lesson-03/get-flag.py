#!/usr/bin/env ./../bin/python3

def caesar(thing_to_encode):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encoded = ''
    for character in thing_to_encode:
        letter_index = alphabet.index(character)
        new_index = letter_index + 13
        if new_index >= 26:
            new_index = new_index - 26
        encoded = encoded + alphabet[new_index]
    return encoded

password = input('Please enter the password: ')

if caesar(password) == 'zbmmneryyn':
    with open('flag.txt', newline='') as f:
        print('The flag is: '+f.read(), end='')

