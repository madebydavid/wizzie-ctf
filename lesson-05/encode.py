#!/usr/bin/env ./../bin/python3

# Tool for hiding the password in the cheese

import random

cheese = []
with open('cheese.txt', 'r') as input_cheese:
    for line in input_cheese:
        line_list = list(line.rstrip())
        cheese.append(line_list)

password = input('Please enter the password to hide in the cheese: ')
positions = []
for character in password:
    hidden_row_position = random.randint(0, len(cheese) - 1)
    hidden_col_position = random.randint(0, len(cheese[0]) - 1)
    cheese[hidden_row_position][hidden_col_position] = character
    positions.append((hidden_row_position, hidden_col_position))

with open('cheese-with-password.txt', 'w') as output_cheese:
    for line in cheese:
        output_cheese.write(''.join(line) + '\n')

print('saved cheese with password to cheese-with-password.txt')

print('positions for letters are:')
print(positions)
