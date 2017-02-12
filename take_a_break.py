# program to choose a youtube video at random
# phil welsby - 12 february 2017

import webbrowser
import random

# list of videos
opeth_01 = 'https://youtube.com/watch?v=qEaf9LqIUZQ'  # windowpane
opeth_02 = 'https://www.youtube.com/watch?v=MDBykpSXsSE'  # ghost of predition
foo_fighters_01 = 'https://www.youtube.com/watch?v=SBjQ9tuuTJQ'  # the pretender
nickleback_01 = 'https://www.youtube.com/watch?v=T3rXdeOvhNE'  # photograph

# print menu to screen
print('''(1)	opeth		windowpane
(2)	opeth		ghost of predition
(3)	foofighters	the pretender	
(4)	nickleback	photograph
''')

# generate a random choice
#choice = random.randint(1, 10)
choice = int(input('Enter your choice'))

# main
if choice == 1:
    webbrowser.open(opeth_01)
elif choice == 2:
    webbrowser.open(opeth_02)
elif choice == 3:
    webbrowser.open(foo_fighters_01)
elif choice == 4:
    webbrowser.open(nickleback_01)
else:
    print('need more videos welsby, pull ya finger out!')
