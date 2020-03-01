#!/usr/bin/env ./../bin/python3
import hashlib

def get_md5(thing_to_encode):
    return hashlib.md5(thing_to_encode.encode()).hexdigest()

password = input('Please enter the password: ')

# clue - the password is a number
if get_md5(password) == '6f3249aa304055d63828af3bfab778f6':
    with open('flag.txt', newline='') as f:
        print('The flag is: '+f.read(), end='')

