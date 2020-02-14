#!/usr/bin/env ./../bin/python3

def reverse(thing_to_reverse):
    new_string = ''
    for character in thing_to_reverse:
        new_string = character + new_string
    return new_string

password = input('Please enter the password: ')

if reverse(password) == 'gnihtemos':
    with open('flag.txt', newline='') as f:
        print('The flag is: '+f.read(), end='')

