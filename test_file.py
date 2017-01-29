# 30th december 2016
# phil welsby

keys = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'a#', 'c#', 'd#', 'f#', 'g#']
key = input('Enter a key: ')
if key in keys:
    print('ok')
else:
    print('I don\'t recognise', key, 'as a musical key')
