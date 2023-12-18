# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 08:45:14 2020

Created by Matthew Morris

Modified on Mon Dec 18 15:20 2023

Modified by kampungkat / AG

"""

# Python for data I
###############################################################################
##                      PYTHON FOR DATA I UNIT01 Advance Drill
###############################################################################
'''Try these from memory, it's OK if it doesn't run keep trying to get it to
work without looking anything up'''
### EXERCISE OUTPUT SIMPLE TEXT ###
# Use the print method and the non print method to create this output'''
Hey, I got this to work!

your solution here
#print method
print("Hey, I got this to work!")

# non-print / python 3 method
("Hey, I got this to work!")

# use end = " " to create this output
Heading1| Heading2| Heading|

your solution here
print("Heading1|", end = " ")
print("Heading2|", end = " ")
print("Heading3|", end = " ")


### EXERCISE Pay calculator ###
# pay = rate * hours worked. Create a calculator for this 
# output should include a string as well. Example output
# I will need to pay petsitter 80

your solution here
hourly_wage = int(input("Enter your wages per hour: $"))
hours = int(input("Enter the number of hours worked last week: "))
pay = hourly_wage * hours
print("I will need to pay", pay)


## EXERCISE
"""
Build a tip calculator with dynamic inputs

Bonus: Once you have the script working copy it and past it into its own script
save it as tipcalc in your pythonscripts folder and try running it from cmd
"""
bill = int(input("Enter the bill amount: $"))
tip_percent = int(input("Enter the tip percentage: %"))
final_bill = round(bill * (1 + tip_percent / 100), 2)
print(f"The final bill is ${final_bill}")


### EXERCISE ###
"""
Add your city and state
Assign log_entry with current_time, my_city, and my_state. 
Sample output for given program 
2014-07-26 02:12:18: Houston Texas

#hint concat or combine was not used in requirements
"""
current_time = '2014-07-26 02:12:18:'
my_city = "Hill View"
my_state = "Singapore"
log_entry = ''' Your solution goes here '''

print(log_entry)



## EXERCISE USE slicing and string functions to bring state back as WA
state = "washington"
'''your solution here'''
state = state[:2].upper()
print(state)


### EXERCISE READING MULTIPLE DATA TYPES ###
q1 = input('What is your name?')
q2 = input('What is your favorite number?') # make this input an integer int()

# concate q1 and q2 into a variable answers

''' Your solution goes here '''
answers = q1 + " and " + q2

print('my answers are: ',answers)



### EXERCISES SLICES and CONCATS PUTTING IT ALL TOGETHER
''' use what you have learned to reformat PO
expected output Loc:860 Date: 11/15/25 Seq:860'''

po = "86011152025001"
''' your solution here'''
loc = po[:3]
dates = po[3:9]
seq = po[-3:]
print(f"Loc:{loc} Date: {dates} Seq:{seq}")


### EXERCISE FIX THE CODE
#Get user's words you can use the % method or format method
relative = input('Enter a type of relative: ')
food = input('Enter a type of food: ')
adjective = input('Enter an adjective: ')
period = input('Enter a time period: ')

# Tell the story
print('My {} says eating {}'.format(relative, food))
print("will make me more {}".format(adjective))
print('so now I eat it every {}'.format(period))




