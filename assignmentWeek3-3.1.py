'''
Use if statement to
calculate pay with entered rate for first 40 hours
and 1.5(entered rate) for overtime
Created on May 3, 2016
@author: dinh
'''

hrs = raw_input('Enter Hours: ')
rate = raw_input('Enter Rate: ')

h = float(hrs)
r = float(rate)
pay = None
if h > 40:
    pay = 40*r + (h-40)*r*1.5
else:
    pay = 40*r

print pay