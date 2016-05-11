'''
Find the max and min of an entered sequence of integers
Created on May 3, 2016
@author: dinh
'''

largest = None
smallest = None
while True:
    num = raw_input("Enter a number or done: ")
    if num == "done":
        break
    try:
        num = int(num)
    except:
        print 'Invalid input'
        continue
    if largest == None or smallest == None:
        largest = num
        smallest = num
        continue
    if largest < num:
        largest = num
    if smallest > num:
        smallest = num

print 'Maximum is', largest
print 'Minimum is', smallest