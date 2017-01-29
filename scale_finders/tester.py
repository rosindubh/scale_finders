# program to find all modes
# started 20th january 2017 - phil welsby
# this is a project under construction it prints all the modes in
# order starting with c to a filoe calles scales
# but needs to write them to a file instead

# individual chromatic scales starting with C
c_chromatic_scale = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#',
                         'A', 'A#','B', 'C', 'C#', 'D']                      
c_sharp_chromatic_scale = ['C#', 'D', 'D#', 'E', 'F','F#', 'G', 'G#',
                           'A','A#', 'B','C', 'C#', 'D', 'D#']
d_chromatic_scale = ['D', 'D#', 'E', 'F','F#', 'G', 'G#', 'A','A#',
                     'B','C', 'C#', 'D', 'D#', 'E']
d_sharp_chromatic_scale = ['D#', 'E', 'F', 'F#', 'G', 'G#','A', 'A#',
                           'B', 'C', 'C#', 'D', 'D#', 'E', 'F']
e_chromatic_scale = ['E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B', 'C',
                    'C#', 'D', 'D#', 'E', 'F', 'F#']
f_chromatic_scale = ['F', 'F#', 'G', 'G#', 'A', 'A#', 'B', 'C', 'C#',
                    'D', 'D#', 'E', 'F', 'F#', 'G']
f_sharp_chromatic_scale = ['F#', 'G', 'G#', 'A', 'A#', 'B', 'C', 'C#',
                           'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']
g_chromatic_scale = ['G', 'G#', 'A', 'A#', 'B', 'C', 'C#', 'D', 'D#',
                    'E', 'F', 'F#', 'G', 'G#', 'A']
g_sharp_chromatic_scale = ['G#', 'A', 'A#', 'B', 'C', 'C#', 'D', 'D#',
                           'E', 'F', 'F#', 'G', 'G#', 'A', 'A#']
a_chromatic_scale = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F',
                    'F#', 'G', 'G#', 'A', 'A#', 'B']
a_sharp_chromatic_scale = ['A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F',
                           'F#', 'G', 'G#', 'A', 'A#', 'B', 'C']
b_chromatic_scale = ['B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G',
                    'G#', 'A', 'A#', 'B', 'C', 'C#']
# list of all the cromatic scales
chromatic_scales = [c_chromatic_scale, c_sharp_chromatic_scale,
                    d_chromatic_scale, d_sharp_chromatic_scale,
                    e_chromatic_scale, f_chromatic_scale,
                    f_sharp_chromatic_scale, g_chromatic_scale,
                    g_sharp_chromatic_scale, a_chromatic_scale,
                    a_sharp_chromatic_scale, b_chromatic_scale]

# all the modes combined into one list starting with ionian
# this is equivalent to the rules of music ie:  T T S T T T S
# for the ionian mode T S T T T S T for dorian etc...
all_modes = [0,2,4,5,7,9,11,12,0,2,3,5,7,9,10,12,0,1,3,5,7,8,10,12,0,2,
             4,6,7,9,11,12,0,2,4,5,7,9,10,12,0,2,3,5,7,8,10,12,0,1,3,5,
             6,8,10,12]

# new line variable                     
new_line = 0

# variable to increment the chromatic scale counter
chromatic_scale_increment = 0

# main
f = open('scales.txt', 'w')
for i in range(12):
    #f = open('scales', 'w')
    for each_item in all_modes:
        s = str(chromatic_scales[chromatic_scale_increment][each_item])
        #print(s)
        f.write(s)
        f.write(' ')
        #print(chromatic_scales[chromatic_scale_increment][each_item], end = ' ')
        new_line+=1
        if new_line > 7:
            #print('\n')
            f.write('\n')
            new_line=0
    chromatic_scale_increment+=1
    #print()
    f.write('\n')
#f.close()                
f.write('''

ionian     = T T S T T T S
dorian     = T S T T T S T
phrygian   = S T T T S T T
lydian     = T T T S T T S
mixolydian = T T S T T S T
aeolian    = T S T T S T T
locrian    = S T T S T T T''')
f.close()
