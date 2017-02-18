#! /usr/bin/python3.4

# rewrite of the Danwood engineer assist program written in 2016
# phil welsby - 16 february 2017 -

import sys
from datetime import datetime

# clear screen function
def wiper():
    print('\n' *80)

# start menu
def start_menu():
    wiper()
    print('''\t\t...WELCOME TO ENGINEER ASSIST...\n\n
    \t\t   Written by Phil Welsby.\n\n\n\t\t\t    2017\n\n\n\n\n''')
    print('\t(1)  Input data\n')
    print('\t(2)  Database search\n')
    print('\t(3)  Run Reports\n')
    print('\t(4)  Car Stock\n')
    print('\t(5)  Create Lists\n')
    print('\t(6)  Retrieve job by line number\n\n')
    print('\t(7)  Exit\n\n')

    try:
        choice = ''
        choice = input('\tEnter a number: ')
        choice = int(choice)
        if choice == 1:
            user_input()
        elif choice == 2:
            search()
        elif choice == 3:
            reports()
        elif choice == 4:
            car_stock_menu()
        elif choice == 5:
            lists()
        elif choice == 6:
            job_retreval()
        elif choice == 7:
            sys.exit()
        else:
            print(choice,'is not a valid option...')
            print()
            input('Press ENTER to continue...')
            start_menu()
    except ValueError:
        start_menu()

def user_input():
    wiper()
    now = datetime.now()
    master_text = open("MASTER.txt", "a")

    # get input from the user
    time = (now.hour, now.minute, now.second)
    date = (now.day, now.month, now.year)
    wiper()
    so = input('Service order number:      ')
    machine_type = input("Machine type:              ")
    fault = input("Fault:                     ")
    cause = input("Cause:                     ")
    action = input("Description of work done:  ")

    parts = input("Parts:                     ")
    submit =  input('\n\nENTER y to SUBMIT or ENTER nothing to ABORT...')
    if submit == 'y':
            # print the inputted data to the text file MASTER.txt
        print("Service Order:", so, "\nDate:", date, "\nTime:", time, "\nMachine type:", machine_type, "\nFault:",fault, "\nCause:",\
        cause, "\nAction:", action, "\nParts:", parts, "\n",file=master_text)
        wiper()
        print('\n\nSUBMITTED')  # pause and update user
        print('The following has been added to the MASTER.txt file\n\n')
        print('Service order number:      ', so)
        print('Machine Type:              ', machine_type)
        print('Fault:                     ', fault)
        print('Cause:                     ', cause)
        print('Description of work done:  ', action)
        print('Parts fitted:              ', parts)
        input('\nEnter to continue')
    else:
        wiper()
        input('\n\nThe data you entered has been ERASED...\nNothing will be written to the file...')
        wiper()
        user_input()

    # close the open file
    master_text.close()
    start_menu() # code added 13/02/2016

start_menu()
