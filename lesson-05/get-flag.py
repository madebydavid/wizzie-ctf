#!/usr/bin/env ./../bin/python3

# Positions for the password
positions = [
    (10, 27),
    (13, 19),
    (1, 40),
    (15, 20),
    (20, 6),
    (12, 19),
    (4, 45),
    (1, 16)
]

# Read the cheese with password
cheese = []
with open('cheese-with-password.txt', 'r') as input_cheese:
    for line in input_cheese:
        line_list = list(line.rstrip())
        cheese.append(line_list)

# Print the cheese with password
for row in cheese:
    print(''.join(row))

# Get the saved password from the cheese
saved_password = ''
for position in positions:
    letter = cheese[position[0]][position[1]]
    saved_password = saved_password + letter

# Compare and show the flag if correct
password = input('Please enter the password: ')
if password == saved_password:
    with open('flag.txt', newline='') as f:
        print('The flag is: '+f.read(), end='')
