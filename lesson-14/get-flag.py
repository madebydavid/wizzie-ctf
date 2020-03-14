#!/usr/bin/env ./../bin/python3
import zipfile

password = input('Please enter the password: ')

try:
    flag_zip = zipfile.ZipFile('flag.zip', 'r')
    flag_zip.extractall(pwd=bytes(password, 'utf8'))
    print('Zip extracted successfully')
except:
    print('Invalid password')
