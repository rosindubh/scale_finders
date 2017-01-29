# example of multiple arguments in a function
# taken from a youtube video https://www.youtube.com/watch?v=WWm5DxTzLuk
# 8 january 2017 - phil welsby

# function to clear the screen
def wiper():
    '''clears the page'''
    print '\n'*50

wiper()

# example 1 -  the use of the *args allows you to insert multiple args in the parenthesis
print 'example 1\n'
print '''def Func_1(*args):
    for arg in args:
        print arg
        
Func_1(1,2,3,54,"ham")\n'''

def Func_1(*args):
    for arg in args:
        print arg

Func_1(1,2,3,54,"ham") # here we call the above function with 
                       # multiple arguments
print
raw_input('press a Enter to continue...\n')
wiper()

# example 2 uses an asterix to print the items in a list
print 'example 2 with an asterix to print items in a list\n'
print '''def Func_2(*args):
    for arg in args:
        print arg
l = [1,2,3,54,"ham"]

Func_2(*l)\n'''

def Func_2(*args):
    for arg in args:
        print arg
l = [1,2,3,54,"ham"]

Func_2(*l) # here we are using Func_2(*l) to print the items in a list
print
raw_input('press a Enter to continue...\n')
wiper()
print 'example 2 without an asterix the list is treated\
 as a single item\n'
print '''def Func_2(*args):
    for arg in args:
        print arg
l = [1,2,3,54,"ham"]

Func_2(l)\n'''
Func_2(l)  # if you call the function Func_2(l) without the * it will print the
           # list as a single item
print
raw_input('press a Enter to continue...\n')
wiper()

# example 3 keyword argument
print 'example 3\n'
print '''def Func_3(x=234, y=9):
    print x, y

Func_3(x=456, y=3)\n'''

def Func_3(x=234, y=9):
    print x, y

Func_3(x=456, y=3) # this will print the values for x and y in the parethesis
print
raw_input('press a Enter to continue...\n')
wiper()

print 'example 3 calls the function with no arguments\n'
print '''def Func_3(x=234, y=9)
    print x, y

Func_3()\n'''

Func_3()           # this will print the default values for x and y as no values
print              # were entered in the parenthesis
raw_input('press a Enter to continue...\n')
wiper()

# example 4 keyword args
print 'example 4\n'
print '''def Func_4(**kwargs):
    for item in kwargs.items():
        print item

Func_4(x=456, y=3, name=\'phil\')\n'''

def Func_4(**kwargs):
    for item in kwargs.items():
        print item

Func_4(x=456, y=3, name='phil')
print
raw_input('press a Enter to continue...\n')
wiper()

# example 5
print 'example 5'
print '''def Func_5(*args, **kwargs):
    for arg in args:
        print arg
    for item in kwargs.items():
        print item

Func_5(1,2,3,4,56,'ham',x=123,y=9)\n'''

def Func_5(*args, **kwargs):
    for arg in args:
        print arg
    for item in kwargs.items():
        print item

Func_5(1,2,3,4,56,'ham',x=123,y=9)

print
print 'Done!'


