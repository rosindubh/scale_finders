# written by phil welsby - 23 january 2017

# program to prove the collatz conjecture
# details can be found in wikipedia at:
# https://en.wikipedia.org/wiki/Collatz_conjecture

# The conjecture can be summarized as follows.
# Take any positive integer n. If n is even, divide it by 2 to get n / 2.
# If n is odd, multiply it by 3 and add 1 to obtain 3n + 1.
# repeat the process indefinatly. The conjecture is that no matter what
# number you start with the final answer is always 1

import sys

# set global variables
steps = 1
number = 0
# get user input

try:
    number = int(input('enter an integer: '))
    saved_number = number
except:
    print('that\'s not an integer an integer is a whole number.')
    sys.exit()

# main
while number != 1:
    if number % 2 == 0:
        number = number/2
        print('number of steps  = ', steps, 'number  = ', number)
        steps += 1
    else:
        number = number * 3 + 1
        print('number of steps  = ', steps, 'number  = ', number)
        steps += 1

print('\nthe integer you chose was', saved_number,
      '\nnumber or steps taken was', steps - 1)

# bit to open a web page on the collatz sequence on wikipedia

while True:
    web_open = input('''\ndo you want to open a wikipedia
web page on the collatz sequence

enter y or n\n''')
    if web_open == 'y':
        import webbrowser
        webbrowser.open('https://en.wikipedia.org/wiki/Collatz_conjecture')
        import sys
        sys.exit()
    elif web_open == 'n':
        import sys
        sys.exit()
