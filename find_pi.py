# User enters a number and the program prints pi to that decimal place

import math

print('***HELLO USER***')
print("Let's find Pi to your amount of decimal places")
user_input = input('Please enter a number between 1 and 10: ')  # Get number as input from the user
print('Pi to the {}th decimal is'.format(user_input), math.pi.__round__(int(user_input)))  # Print Pi to the decimal place provided by the user
