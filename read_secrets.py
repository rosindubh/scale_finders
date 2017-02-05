# written while watching Coding is for girls
# 5 february 2017 - phil welsby
# web address - https://www.youtube.com/watch?v=t2HWbunxKIQ

import os

check_file = True
path_to_file = '/home/phil/Desktop/secret.txt'

while check_file:
    file_exists = os.path.exists(path_to_file)
    if file_exists:
        print('secret.txt file exists')
        secret_file = open(path_to_file, 'r+')
        for line in secret_file:
            print(line)
        secret_file.write('I know your secrets\n')
        secret_file.close()

        check_file = False


