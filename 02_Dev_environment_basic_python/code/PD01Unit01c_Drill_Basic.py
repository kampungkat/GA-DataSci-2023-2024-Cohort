# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 07:49:08 2020

@author: msmorris

Modified on Mon Dec 18, 15:00 2023

@modifier: kampungkat / AG
"""

###############################################################################
##                      PYTHON FOR DATA I Unit 1 Cheat Sheet
###############################################################################
#Finish each cheatsheet section without looking at the cheatsheet, Whats missing

# one line comment
''' multiple line comment'''

print("header1")
print("header2")

# Printing a variable
cost = 9
print(cost)

# Concating variables an strings using a comma
cost = 24.00
tip = .2
total = cost + (cost * tip)
print("I should tip:", total)


username = input() #enter a name in the console and hit Enter

# converting input types
int() integer
str() string
float() float

hours = '40'
wage = 20
salary = int(hours)  * wage


#convert an input into an integer
wage = int(input("Enter wage :"))


#slicing   
pet = 'Cat'
print(pet[0]) #expected output C
print(pet[0], pet[1], pet[2])# Expected output C a t
print(pet[:3]) # Expected output Cat
print(pet[-1]) #Expected output t
print(pet[-2:]) #Expected output at



# concatenating ()
print("hello" ) # add a seperate string "there and concatenate in same print
print(str(5) + ' there')   # cast 5 to a string in order for this to work


# uppercasing
state = "washington"
state.upper()      # make state uppercase
state.capitalize()        # make state title case


## imputing variables into a string 2 methods
# %d Substitute integer
# %f floating point
# %s string
# %x, %X hexadecimal x lower X upper
# %e, %E floating point exponential format e lower E upper
# %r raw
a = 'cats'
b = 'dogs'
c = 5

print("I have %d %s and %d %s") %(c,b,c,a)



# Using format to accomplish the same task
a = 'cats'
b = 'dogs'
c = 5
("I have {} {} and {} {}").format(c, b, c, a)

x = "fun"
print("Mad_libs is a {} game".format(x))

##Example 2
print("Mad_libs is a {} {}".format("fun","game"))