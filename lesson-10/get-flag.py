#!/usr/bin/env ./../bin/python3
import time

def get_approximate_time():
    timestamp = int(time.time() / 10)
    return timestamp

password = input('Please enter the password: ')

if int(password) == get_approximate_time():
    with open('flag.txt', newline='') as f:
        print('The flag is: '+f.read(), end='')

