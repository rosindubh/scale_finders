# program to find any mode in any key
# started a rewrite 30 december 2016 - phil welsby
# improved and added menu's 22 january 2017 - phil welsby
# uploaded to python anywhere 23 january 2017

import sys

# wiper
def wiper():
    print('\n'*40)
# chromatic scales
c_cromatic_scale = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B', 'C']
c_sharp_chromatic_scale = ['C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B', 'C', 'C#']
d_cromatic_scale = ['D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B', 'C', 'C#', 'D']
d_sharp_chromatic_scale = ['D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B', 'C', 'C#', 'D', 'D#']
e_cromatic_scale = ['E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E']
f_cromatic_scale = ['F', 'F#', 'G', 'G#', 'A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F']
f_sharp_chromatic_scale = ['F#', 'G', 'G#', 'A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#']
g_cromatic_scale = ['G', 'G#', 'A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G']
g_sharp_chromatic_scale = ['G#', 'A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']
a_cromatic_scale = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A']
a_sharp_chromatic_scale = ['A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#']
b_cromatic_scale = ['B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']

# modes
ionian = [0,2,4,5,7,9,11,12]
dorian = [0,2,3,5,7,9,10,12]
phrygian = [0,1,3,5,7,8,10,12]
lydian = [0,2,4,6,7,9,11,12]
mixolydian = [0,2,4,5,7,9,10,12]
aeolian = [0,2,3,5,7,8,10,12]
locrian = [0,1,3,5,6,8,10,12]

def scale_finder():    # print mode menu to screen
    print('''\n\n\t\t\t MODES MENU


    \t1) IONIAN
    \t2) DORIAN
    \t3) PHRYGIAN
    \t4) LYDIAN
    \t5) MIXOLYDIAN
    \t6) AEOLIAN
    \t7) LOCRIAN\n\n\n''')
    wiper()
    # key menu
    print('''\t\t\t KEY\'s MENU


    \tC \tenter a c and press enter
    \tC# \tenter a c# and press enter
    \tD \tenter a d and press enter
    \tD# \tenter a d# and press enter
    \tE \tenter an e and press enter
    \tF \tenter an f and press enter
    \tF# \tenter an f# and press enter
    \tG \tenter a g and press enter
    \tG# \tenter a g# and press enter
    \tA \tenter an a and press enter
    \tA# \tenter an a# and press enter
    \tB \tenter a b and press enter\n\n
    To quit enter 999 then press enter...\n\n''')
    # choose a key
    key = input('Enter a musical key: ')
    key = key.lower()
    if key == 'c':
        key = c_cromatic_scale
    elif key == 'c#':
        key = c_sharp_chromatic_scale
    elif key == 'd':
        key = d_cromatic_scale
    elif key == 'd#':
        key = d_sharp_chromatic_scale
    elif key == 'e':
        key = e_cromatic_scale
    elif key == 'f':
        key = f_cromatic_scale
    elif key == 'f#':
        key = f_sharp_chromatic_scale
    elif key == 'g':
        key = g_cromatic_scale
    elif key == 'g#':
        key = g_sharp_chromatic_scale
    elif key == 'a':
        key = a_cromatic_scale
    elif key == 'a#':
        key = a_sharp_chromatic_scale
    elif key == 'b':
        key = b_cromatic_scale
    elif key == '999':
        sys.exit()
    else:
        print(key, 'is not a key...')
        input('Press a key to continue')
        scale_finder()


    # mode menu
        # print mode menu to screen
    print('''\n\n\t\t\t MODES MENU

To select a mode you must enter the full name of the mode.
eg:
To select the ionian mode type IONIAN in either upper or lower case\n\n\n
    \t1) IONIAN
    \t2) DORIAN
    \t3) PHRYGIAN
    \t4) LYDIAN
    \t5) MIXOLYDIAN
    \t6) AEOLIAN
    \t7) LOCRIAN\n\n\n''')
    print()
    print('''MODES''')
    # choose a mode
    mode = input('Enter a mode: ')
    mode = mode.lower()
    if mode == 'ionian':
        mode = ionian
    elif mode == 'dorian':
        mode = dorian
    elif mode == 'phrygian':
        mode = phrygian
    elif mode == 'lydian':
        mode = lydian
    elif mode == 'mixolydian':
        mode = mixolydian
    elif mode == 'aeolian':
        mode = aeolian
    elif mode == 'locrian':
        mode = locrian
    else:
        print(mode, 'is not a mode')
        input('Press a key to continue')
        scale_finder()




    # print chosen scale
    for note in mode:
        print(key[note].upper(), end=' ')
    print()
    input('Press a key to continue')
    scale_finder()
    
scale_finder()



        
