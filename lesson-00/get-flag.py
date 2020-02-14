#!/usr/bin/env ./../bin/python3

password = input('Please enter the password: ')

if password == 'letmein':
    with open('flag.txt', newline='') as f:
        print('The flag is: '+f.read(), end='')

