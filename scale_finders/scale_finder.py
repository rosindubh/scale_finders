# program to find any modal scale in music
# 19 December 2016 - phil welsby

import sys

def restart():
    print('\nPress enter to continue...\n')
    input()
    scale_finder()

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

def scale_finder():
    for i in range(50):
        print()

# key menu
    print('''\t\t\t KEY\'s MENU


    \tC \tenter a 1 and press enter
    \tC# \tenter a 2 and press enter
    \tD \tenter a 3 and press enter
    \tD# \tenter a 4 and press enter
    \tE \tenter a 5 and press enter
    \tF \tenter a 6 and press enter
    \tF# \tenter a 7 and press enter
    \tG \tenter a 8 and press enter
    \tG# \tenter a 9 and press enter
    \tA \tenter a 10 and press enter
    \tA# \tenter a 11 and press enter
    \tB \tenter a 12 and press enter\n\n
    To quit enter 999 then press enter...\n\n''')
    
    # get user to choose a key
    while True:
        try:
            key = int(input('Choose a KEY -> '))
            if key == 1:
                scale = c_cromatic_scale
                break
            elif key == 3:
                scale = d_cromatic_scale
                break
            elif key == 5:
                scale = e_cromatic_scale
                break
            elif key == 6:
                scale = f_cromatic_scale
                break
            elif key == 8:
                scale = g_cromatic_scale
                break
            elif key == 10:
                scale = a_cromatic_scale
                break
            elif key == 12:
                scale = b_cromatic_scale
                break
            elif key == 2:
                scale = c_sharp_chromatic_scale
                break
            elif key == 4:
                scale = d_sharp_chromatic_scale
                break
            elif key == 7:
                scale = f_sharp_chromatic_scale
                break
            elif key == 9:
                scale = g_sharp_chromatic_scale
                break
            elif key == 11:
                scale = a_sharp_chromatic_scale
                break
            elif key == 999:
                print('Goodbye please come back soon.')
                sys.exit()
            else:
                print('That is not a valid number')
        except ValueError:
            print('\nTo choose a key, enter the number next to that key,')
            print('and then press the ENTER key.')
            print('Please try again...\n')


    # print mode menu to screen
    print('''\n\n\t\t\t MODES MENU


    \t1) IONIAN
    \t2) DORIAN
    \t3) PHRYGIAN
    \t4) LYDIAN
    \t5) MIXOLYDIAN
    \t6) AEOLIAN
    \t7) LOCRIAN\n\n\n''')

    # get user to choose a mode and print result to screen
    while True:
        try:
            mode = int(input('Choose a mode -> '))
            print('\n\n')
            if mode == 1:
                mode = ionian
                for note in ionian:
                    print(scale[note], end=' ')
            elif mode == 2:
                mode = dorian
                for note in dorian:
                    print(scale[note], end=' ')
            elif mode == 3:
                mode = phrygian
                for note in phrygian:
                    print(scale[note], end=' ')
            elif mode == 4:
                mode = lydian
                for note in lydian:
                    print(scale[note], end=' ')
            elif mode == 5:
                mode = mixolydian
                for note in mixolydian:
                    print(scale[note], end=' ')
            elif mode == 6:
                mode = aeolian
                for note in aeolian:
                    print(scale[note], end=' ')
            elif mode == 7:
                mode = locrian
                for note in locrian:
                    print(scale[note], end=' ')
            else:
                print('That is not a valid number...')
        except ValueError:
            print('choose a number between 1-7')
        restart()



scale_finder()
        
        
      
