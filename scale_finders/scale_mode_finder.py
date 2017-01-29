# program to find scale modes for the piano or the trumpet
# started wednesday 18th january 2017 - phil welsby

# function to clear screen
def wiper():
    print('\n'*50)
wiper()
trumpet_cromatic_scale = ['C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab', 'A', 'Bd',
                  'B', 'C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab', 'A',
                  'Bd', 'B']
piano_chromatic_scale = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#',
                      'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A',
                      'A#', 'B']



# modes variables
ionian = [0,2,4,5,7,9,11,12]
dorian = [0,2,3,5,7,9,10,12]
phrygian = [0,1,3,5,7,8,10,12]
lydian = [0,2,4,6,7,9,11,12]
mixolydian = [0,2,4,5,7,9,10,12]
aeolian = [0,2,3,5,7,8,10,12]
locrian = [0,1,3,5,6,8,10,12]


# get user to choose an instrument type
while True:
    wiper()
    try:
        print('Choose an instrument 1 for a piano, 2 for a B flat trumpet.')
        instrument = int(input('Choose piano or trumpet: '))
        if instrument == 1:
            instrument = 0
            break
        elif instrument == 2:
            instrument = -2
            break
    except:
        wiper()
        print('\nyou must enter either a 1 or a 2...')
        input('Please press Enter to continue. ')
        




# MODES Section  

while True:
    wiper()
    # print mode menu to screen
    print('''\n\n\t\t\t MODES MENU


    \t1) IONIAN
    \t2) DORIAN
    \t3) PHRYGIAN
    \t4) LYDIAN
    \t5) MIXOLYDIAN
    \t6) AEOLIAN
    \t7) LOCRIAN\n\n\n''')
    
    # get user to choose a mode
    try:
        mode = int(input('Choose a mode: '))
        if mode > 0 and mode < 8:
            break
        else:
            print('You must enter a number between 1 and 7.')
            input('Press Enter to continue...')
            
    except:
        print('You must enter a number between 1 and 7.')
        input('Press Enter to continue')

if mode == 1:
    mode = ionian
elif mode == 2:
    mode = dorian
elif mode == 3:
    mode = phrygian
elif mode == 4:
    mode = lydian
elif mode == 5:
    mode = mixolydian
elif mode == 6:
    mode = aeolian
elif mode == 7:
    mode = locrian



####################       ok up to here     #########################
# need to set up try except to catch exceptions for key input,       #
# and variables for instrument, key and mode so that these are       #
# printed out at the end as in:-                                     #
#                                  key = C#                          #
#                                 mode = phrygian                    #
#                           instrument = trumpet                     #
# this will remind the user what they chose                          #
#######################################################################

# get user to choose a key
# key menu
wiper()
print('''\t\t\t KEY\'s MENU


\tC \tenter a 0 and press enter
\tDb \tenter a 1 and press enter
\tD \tenter a 2 and press enter
\tEb \tenter a 3 and press enter
\tE \tenter a 4 and press enter
\tF \tenter a 5 and press enter
\tGb \tenter a 6 and press enter
\tG \tenter a 7 and press enter
\tAb \tenter a 8 and press enter
\tA \tenter a 9 and press enter
\tBd \tenter a 10 and press enter
\tB \tenter a 11 and press enter\n\n''')
key = int(input('Enter a key: '))

# print result
wiper()
print()
print('flats')
for item in mode:
    print(trumpet_cromatic_scale[item + key + instrument], end=' ')
print()
print('sharps')
for item in mode:
    print(piano_chromatic_scale[item + key + instrument], end=' ')
print('\n'*5)
    


