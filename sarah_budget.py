# program to add up sarah's outgoings against her income
# and print results to the screen
# 8 march 2016 - phil welsby

# income
income = float(input('Enter wages: £'))
child_benifit = 88
tax_credits = 300
kali = 200
total_income = income + child_benifit+tax_credits+kali

# outgoings
car_debt = 150
rent = 100
insurance = 150
car_tax = 15
other_debt = 50
gym = 17.99
union = 10
bank_charges = 36
child_minding = 100
savings = 25
AA = 10
total_out = car_debt+rent+insurance+car_tax+other_debt+gym+union+bank_charges+child_minding+savings+AA

# results
print('Total income:        ', total_income)
print('Total outgoings:      ', total_out)
disposable = total_income - total_out
print('Disposable income is: ', disposable)

