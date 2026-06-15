from datetime import date

current_year = date.today().year
birth_year = int(input('What is your birth year? '))

age = current_year - birth_year

if age == 18:
    print('You are at the enlistment age. Enlist now!')
elif age > 18:
    print('You are {} years past the enlistment age.'.format(age - 18))
else:
    print('You will need to enlist in {} years.'.format(18 - age))
