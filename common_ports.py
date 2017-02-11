#!/usr/bin/python3
# program to show a description of the most common ports
# phil welsby - 11 february 2017
def wiper():
    print('\n' * 100)
wiper()
file = open('common_port_numbers.txt')
port_number = input('Enter a port number: ')

for each_line in file:
    if not each_line.find(':') == -1:
        (number, description) = each_line.split(':', 1)
        if port_number == number:
            print()
            print('Common use for port', port_number, 'is...', description)
file.close()
