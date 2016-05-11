'''
Use if statement to assign grade to entered score
Created on May 3, 2016
@author: dinh
'''

score = raw_input('Enter score between 0.0 and 1: ')
score = float(score)
if score < 0 or score > 1:
    print 'Score out of range. Exit.'
    quit()
grade = None
if score >= 0.9:
    grade = 'A'
elif score >= 0.8:
    grade = 'B'
elif score >= 0.7:
    grade = 'C'
elif score >= 0.6:
    grade = 'D'
else:
    grade = 'F'
print grade