import webbrowser

#xs_radio = webbrowser.open('http://www.xsmanchester.co.uk/radio/player/')
#bbc_manchester = webbrowser.open('http://www.bbc.co.uk/radio/player/bbc_radio_manchester')

print('''\t(1)\txs radio
\t(2)\tbbc radio manchester''')
choice = int(input('Enter a number to choose: '))

if choice == 1:
    webbrowser.open('http://www.xsmanchester.co.uk/radio/player/')
elif choice == 2:
    webbrowser.open('http://www.bbc.co.uk/radio/player/bbc_radio_manchester')
