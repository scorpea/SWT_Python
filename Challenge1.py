# python program challenge
from datetime import date

fname = input('what is your First Name? ')
lname = input('what is your Last Name? ')
byear = input('what is your birth year? ')
addr = input('what is your Address? ')
sex = input('what is your gender M/F ')
weigh = input('what is your weight in kg? ')
nation = input('what is your nationality ')

wpound = float(weigh) // 0.45

# creating the date object of today's date
todays_date = date.today()

# fetching the current year
cyear =  todays_date.year
age = cyear - int(byear)

if sex.upper() == 'M' :
    s1 = 'He'
    sex = 'Male'
else :
    s1 = 'She'
    sex = 'Female'

print('First Name: ', fname)
print('Last Name: ', lname)
print('Address: ',addr)
print('Weight in Kg:',weigh)
print('Age:',age)
print('Nationality:', nation)
print('Sex:', sex)

print(fname, lname,'lives at', addr+'.',s1, 'weighs',int(wpound), 'in pounds and',weigh, 'in kg.',s1, 'comes from', nation)
