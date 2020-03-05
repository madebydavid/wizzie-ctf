#!/usr/bin/env ./../bin/python3
import hashlib

def get_md5(thing_to_encode):
    return hashlib.md5(thing_to_encode.encode()).hexdigest()

salt = "spice"
password = input('Please enter the password: ')

# clue - the password is STILL a number
if get_md5(salt + password) == 'c9d0da3ce98f449ef65cfa11db8508a7':
    with open('flag.txt', newline='') as f:
        print('The flag is: '+f.read(), end='')

