#!/usr/bin/env ./../bin/python3

def change_alphabet(thing_to_encode):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    new_alphabet = 'xwqztayeunoifbkvslpgdcjmhr'
    encoded = ''
    for character in thing_to_encode:
        letter_index = alphabet.index(character)
        encoded = encoded + new_alphabet[letter_index]
    return encoded

password = input('Please enter the password: ')

if change_alphabet(password) == 'qetzzxl':
    with open('flag.txt', newline='') as f:
        print('The flag is: '+f.read(), end='')

