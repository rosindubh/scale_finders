# program to determine disposable income for the month
# 8 january 2017 - phil welsby

# clear screen

print('\n'*100)

# monthly costs excluding food
gas=float(11.26)
electricity=float(128.00)
water=float(33.48)
council_tax=float(104.00)
dentist=float(37.70)
tv_licence=float(12.12)
mortgage=float(424.21)
netflix=float(7.49)
virgin_media=float(33.46)
now_tv_1=float(6.99)
now_tv_2=float(2.99)
home_insurance_1=float(15.58)
home_insurance_2=float(20.11)

# total of outgoings
total_outgoings=gas+electricity+water+council_tax+dentist+tv_licence+mortgage+\
netflix+virgin_media+now_tv_1+now_tv_2+home_insurance_1+home_insurance_2

# print to screen
print('outgoings:')
print()
print('gas              =  ', gas)
print('electricity      = ', electricity)
print('water            =  ', water)
print('council tax      = ', council_tax)
print('dentist          =  ', dentist)
print('tv licence       =  ', tv_licence)
print('mortgage         = ', mortgage)
print('netflix          =   ', netflix)
print('virgin media     =  ', virgin_media)
print('now tv 1         =   ', now_tv_1)
print('now tv 2         =   ', now_tv_2)
print('home insurance 1 =  ',home_insurance_1)
print('home insurance 2 =  ',home_insurance_2)
print()
print('total outgoings  = ',total_outgoings)

# function to compute disposable income

def salary():
    while True:
        try:
            salary = float(input('enter this months salary: '))
            disposable_income=salary - total_outgoings
            print('disposable income this month is = ', disposable_income)
            break
        except ValueError:
          #  salary()
          print('Please try again...')
      

salary()

