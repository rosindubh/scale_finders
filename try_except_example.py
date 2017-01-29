# example of exception handling
# 9 january 2017 - phil welsby

while True:
    try:
        x=int(input('Enter an integer: \n'))
        print('The interger you entered was:',x)
        break
    except:
        print('That is not an integer,\nplease try again...\n')

