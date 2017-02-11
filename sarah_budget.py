# program to add up sarah's outgoings against her income
# and print results to the screen
# 8 march 2016 - phil welsby

# income
income = float(input('Enter wages: £'))
child_benifit = 82
tax_credits = 510
working_tax_credits = 158
kali = 200
total_income = income + child_benifit+tax_credits+kali+working_tax_credits

# outgoings
phone = 40
union = 12
car_tax = 16
car_insurance = 160
rent = 210
gas = 30
water = 30
electric = 40
council_tax = 60
nursery = 300
tv_licence = 30
other_debts =50
AA = 15
total_out = phone+union+car_tax+car_insurance+rent+gas+water+electric+council_tax+nursery+tv_licence+other_debts+AA

# results
print('Total income:        ', total_income)
print('Total outgoings:      ', total_out)
disposable = total_income - total_out
print('Disposable income is: ', disposable)

