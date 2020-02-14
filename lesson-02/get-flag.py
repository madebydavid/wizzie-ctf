#!/usr/bin/env ./../bin/python3

password = input('Please enter the password: ')

if int(password) + 247 == 31337:
    with open('flag.txt', newline='') as f:
        print('The flag is: '+f.read(), end='')

