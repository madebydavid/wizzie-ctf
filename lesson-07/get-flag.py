#!/usr/bin/env ./../bin/python3

a = 'still'
b = 'moon'
c = 'catapult'

saved_password = a[:3] + c[-2:] + b[1] + b[3]

password = input('Please enter the password: ')

if password == saved_password:
    with open('flag.txt', newline='') as f:
        print('The flag is: '+f.read(), end='')

