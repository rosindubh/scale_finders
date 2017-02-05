# program to choose a Netflix Genre web page from codes printed in the manchester evening news
# 5 february 2017


import webbrowser

path = '/home/phil/my_python_programs/netflix_codes'

code =input('enter code: ')
webbrowser.open('http://www.netflix.com/browse/genre/' + code)

#with open(path) as codes_file:
#    for line in codes_file:
#        print(line)
