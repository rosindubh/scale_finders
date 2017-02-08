# program to find the calendar for any month and year
# phil welsby - 8 february 2017
import calendar
m = int(input('enter month: '))
y = int(input('enter year: '))
cal = calendar.month(y, m)
print(cal)
