# program to choose a youtube video at random
# phil welsby - 12 february 2017

import webbrowser
import random

# function to clear screen
def wiper():
    print('\n' * 50)

wiper()

# list of videos
opeth_01 = 'https://youtube.com/watch?v=qEaf9LqIUZQ'  # windowpane
opeth_02 = 'https://www.youtube.com/watch?v=MDBykpSXsSE'  # ghost of predition
foo_fighters_01 = 'https://www.youtube.com/watch?v=SBjQ9tuuTJQ'  # the pretender
nickleback_01 = 'https://www.youtube.com/watch?v=T3rXdeOvhNE'  # photograph
gorillaz_01 = 'https://www.youtube.com/watch?v=HyHNuVaZJ-k'  # feel good inc
my_chemical_romance_01 = 'https://www.youtube.com/watch?v=RRKJiM9Njr8'
greenday_01 = 'https://www.youtube.com/watch?v=NUTGr5t3MoY'
nirvana_01 = 'https://www.youtube.com/watch?v=hTWKbfoikeg'
xs_radio = 'http://www.xsmanchester.co.uk/radio/player/'
radio_manchester = 'http://www.bbc.co.uk/radio/player/bbc_radio_manchester'
# print menu to screen
print('''
		  ***YouTube Videos***


	(1)	opeth			windowpane
	(2)	opeth			ghost of predition
	(3)	foofighters		the pretender	
	(4)	nickleback		photograph
	(5)	gorillaz		feel good inc
	(6)	my chemical romance	welcome to the black parade
	(7)	greenday		basket case
	(8)	nirvana			smells like teen spirit

		      ***Local Radio***

	(9)	xs radio		local radio
	(10)	radio manchester	local radio


''')

# generate a random choice
#random_choice = random.randint(1, 10)

# get user to choose a vid
choice = int(input('Enter your choice: '))

# main
if choice == 1:
    webbrowser.open(opeth_01)
elif choice == 2:
    webbrowser.open(opeth_02)
elif choice == 3:
    webbrowser.open(foo_fighters_01)
elif choice == 4:
    webbrowser.open(nickleback_01)
elif choice == 5:
    webbrowser.open(gorillaz_01)
elif choice == 6:
    webbrowser.open(my_chemical_romance_01)
elif choice == 7:
    webbrowser.open(greenday_01)
elif choice == 8:
     webbrowser.open(nirvana_01)
elif choice == 9:
    webbrowser.open(xs_radio)
elif choice == 10:
    webbrowser.open(radio_manchester)

else:
    print('need more videos welsby, pull ya finger out!')
