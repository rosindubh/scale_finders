# program to take details of home network and print to a file
# phil welsby - 22 february 2017


data = open('network_details.txt', 'a')

device = input('DEVICE NAME: ')
wired_mac = input('WIRED MAC ADDRESS: ')
w_less_mac = input('WIRELESS MAC ADDRESS: ')
wired_ip = input('WIRED IP ADDRESS: ')
w_less_ip = input('WIRELESS IP ADDRESS: ')
print('device:', device, '\nwired mac address:', wired_mac, '\nwireless mac address:', w_less_mac, '\nwired ip address:', wired_ip,\
'\nwireless ip address:', w_less_ip, '\n', file = data)

data.close()

