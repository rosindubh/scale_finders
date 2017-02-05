# written while watching Coding is for girls
# 5 february 2017 - phil welsby

import csv

csv_file = open('google_stock_data.csv')
csv_reader = csv.reader(csv_file, delimiter=',')
next(csv_reader)

for row in csv_reader:
    print(row)

csv_file.close()

