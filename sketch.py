# code from Head First Python
# phil welsby - 18 april 2017

file = open('sketch.txt')
for line in file:
    (role, line_spoken) = line.split(':', 1)
    print(role, end='')
    print(' said: ', end='')
    print(line, end='')
file.close()

