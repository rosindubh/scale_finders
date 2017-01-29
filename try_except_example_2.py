# taken from python errors and exceptions tutorial
# https://docs.python.org/3.4/tutorial/errors.html
# 10 january 2017 - phil welsby

import sys

try:
    f = open('myfile.txt')
    s = f.readline()
    i = int(s.strip())
except OSError as err:
    print('OS error: {0}'.format(err))
except ValueError:
    print('Could not convert data to an integer.')
except:
    print('Unexpected error:', sys.exc_info()[0])
    raise
