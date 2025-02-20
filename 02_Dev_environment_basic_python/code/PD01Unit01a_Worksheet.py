# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 14:45:21 2020

@author: msmorris
"""

"""
Modified on Sun Feb 17 22:50:00 2023

@editor: kampungkat / AG
"""

# Python for data I
# Matthew Morris 
###############################################################################
##                      PYTHON FOR DATA I
## UNIT 1 SETUP, PROGRAMMING PRINCIPLES, PRINT_INPUT, ERRORS, INTRO TO STRINGS
## UNIT 2 MATH AND 3 VALUE LOGIC(IF, THEN, ELSE)
## UNIT 3 FUNCTIONS
## UNIT 4 WORKING WITH FILES
## UNIT 5 DATA STRUCTURES
## UNIT 6 LOOPS AND LISTS
##
## The class is desinged to be a loop, once you finish you can start over
## and continue to build your program and skills. 
###############################################################################
'''
Script are eventually meant to be run. 
Starting out you can do this from a few different places 
Primarly because, each person may have different setups for their computer. 
You can have various instances of Python running, firewall issues, versions of
operating systems. 
Keeping this in mind you may not get configured straight way with the below instructions

If that is the case for you, it might mean some troubleshooting. 
Try these links
https://geek-university.com/python/add-python-to-the-windows-path/
https://stackoverflow.com/questions/34030373/anaconda-path-environment-variable-in-windows

1) Create a folder where you will put all of your python scripts

2) Set up your environment variable

This worked for me but it may not work exactly for you. 
  a) Use windows browser to locate your Anaconda folder
  b) Go to start prompt right click and choose run
  c) type sysdm.cpl and OK to open system properties
  d) click on the Advanced tab
  e) click on the Environment Variables... button
  f) In the bottom window, System Variables, choose Path and click New
  g) Click new and type in the Path to your Anaconda folder. 
      ie C:\Users\yourname\AppData\Local\Continuum\anaconda3
      # Note browse does not work well. You will want to type this in.

3) test your Set up
  a) in your pythonscripts folder create a new .txt
  b) copy and past the below statement

def test1():
    print('This is test1')
test1()
input('Press ENTER to exit')

  c) Save file as test1.py
  d) Close file
  e) From start menu open new Anaconda Prompt(make sure old ones are close)
  f) using CD navigate to your python scripts folder
  g) type name of script plus extensions test1.py
  h) you should see This is test1

If you have run the above and it is not working you can still go through the class
unfortunatly troubleshooting can take a long time so try the links above after class
if you are having any issues.

You will still be able to test most code in the spyder consol. 
In your start menu run anaconda command prompt 
Navigate using CD change directory to where your scripts are stored.

You may need to associate your scripts to the python executable(python.exe)
Not the funnest configuring everything but once your done, it's programming time!
'''
###############################################################################
##                      PYTHON FOR DATA I - UNIT 1
##               PROGRAMMING PRINCIPLES, INTRO TO STRINGS
## COMMENTING
## PROGRAMMING PRINCIPLES
## STRINGS
## PROJECT EXERCISE 
###############################################################################


########################COMMENTING YOUR CODE###################################

# Enter one line of comments
''' 
Enter
Multiple 
Lines 
Of
Comments
'''


'''
in 
'''

'''
print("We are in a comment")
print ("We are still in a comment")
'''
print("We are out of the comment")

###############################################################################
##                       NICE HEADERS                                        ##
###############################################################################


print('we wont be learning Hello World') # we want to divide nlc by cost


## More on Commenting
'''
You should comment before each new section of code and can even comment line 
by line. Aside from that whenever you have a breakthrough; comment instructions
on what you did for your future self to remember. Write your comment as though
someone who does not read code would understand what the code is doing from 
your comment. 
'''
# Commenting out code
print("Not a comment")
# print("I'm a comment") notice using the # to comment out code you don't want to run

# My style of header
###############################################################################
##                          NAME OF PROGRAM                                  ##
###############################################################################
## Requester:                              Department/Division
## Documentation: url://docs//...
## Created by:
## Created by:
## Created by:
##
''' Purpose:




'''
##-----------------------------------------------------------------------------
##                            Source tables                                  ##
##-----------------------------------------------------------------------------
##
##
##
##----------------------------------------------------------------------------- 
##                         calcs/business rules                              ##
##-----------------------------------------------------------------------------
##
##
##
##-----------------------------------------------------------------------------
##                             CHANGE LOG                                    ##
##-----------------------------------------------------------------------------
## DATE | FIRST NAME | LAST NAME      |CHANGE MADE
##
##
###############################################################################


  
########################PROGRAMMING PRINCIPLES#################################

# PYTHON PHILOSOPHY
'''
Beautiful is better than ugly
Explicit is better than implicit
Simple is better than complex
Complex is better than complicated
Readability counts
to read all of the python philosphy simply run import this.
'''
import this #Restart kernal to display again, and again

# more documentation https://www.python.org/doc/

####################VOCABULARY#################################################
'''
There are a lot of new terms to learn here are just a few to get started

LIBRARY
Python library is a collection of functions and methods that allows you to 
perform many actions without writing your code. MATH is one of the core libraries 
for several math functions. Who wants to figure out standard deviation long hand?

Concept: import a library building
Syntax: import library


MODULE import 
a file consisting of Python code. A module can define functions, classes and 
variables. A module can also include runnable code.

Concept: from the library building import math books
Syntax: from library import math

OR

you could Import the entire library at the top of the code and throughout the code
reference pieces you want to use

Syntax:           import library
later in code     library.math

FUNCTION f() 
reusable code, sometimes called a method (object oriented programming)
A process for making something. IE recipe for pizza
Syntax 
def make_pizza():
    code does something
make_pizza()    

CLASSES 
A class is a code template for creating objects
design for a car

OBJECTS 
instance of a class 
actual car created from design

EXPRESSIONS - returns a value 
STATEMENTS - statement is a line of code
 1 statement per line while code line reduction is good multiple statements
 per line is not
'''

##EXAMPLES OF GOOD CODE VS BAD CODE

# Explicit verses implicit
4+4*4-4
(4+4)*4-4
4+4*(4-4)
(4+4)*(4-4)

(( 4 + (4 * 4)) - 4)

# Good code
import platform
print(platform.python_version())
print("let's get to the hands on exercises!")

# Better code
import platform
print ((platform.python_version())+" "+("let's get to the hands on exercises!"))

# Bad code
import platform
print(platform.python_version()); print("let's get to the hands on exercises")

## CODING USES CODING USES CODING
# Brief over view of coding 
# variables
x = 1
y = 1
x + y

#Payday calc
wage = 15
hours = 40
weeks = 50
salary = wage * hours * weeks
print(salary)



# like the above you will build functions that call functions
def traffic_cop():
    go()
    
def go():
    print("wave cars to go")

traffic_cop()




###############################################################################
##                             PRINT                                        ##
###############################################################################
"""
Printing of output to a screen is a common programming task. 
There are a few ways to display output for now lets look at print
"""
print("here is one way, text in quotes that is also in parentheses or parens")
("this is the same as above but you don't need print this is just of Python 3")

"""
end=' ', puts output on the same line separated by a single space. 
"""
print("check", end=" ")
print("it", end = " ")
print("out", end = " ")

# creating a csv and need to comma delimiters
print("check", end=",")
print("it", end = ",")
print("out", end = ",") # you can use this for any delimiter pipe, space etc

"""
single or double quotes work. However, double quotes are pretty nice when you 
have things like "you're". Rule of thumb use double quotes with complex strings
and single for simple. 
"""
### EXERCISE OUTPUT SIMPLE TEXT ###

# Use the print method and the non print method to create this output'''
Hey, I got this to work!

your solution here
#this is the print method
print("Hey, I got this to work!")

#AG --> The above output returns a standard reponse, probably more elegant

#this is the non-print / pythonic 3.0 method
("Hey, I got this to work!")

#AG --> The pythonic method seems to return an STDOUT response

# use end = " " to create this output
Heading1| Heading2| Heading|

your solution here

print("Heading1|", "xyz", end="abc")
print("Heading2|", end=" ")
print("Heading3|", end=" ")

"""AG --> The comma ',' is like a separator, similar to the plus '+'
However, the comma doesn't join / concatenate - there is a single whitespace left
between the two objects
"""

# Printing a variable
cost = 24.00
tip = .2
total = (cost + (cost * tip))
print(total)

# Concating variables an strings using a comma
cost = 24.00
tip = .2
total = cost + (cost * tip)
print("My total with tip is :", total )

### EXERCISE Pay calculator ###
# pay = rate * hours worked. Create a calculator for this 
# output should include a string as well. Example output
# I will need to pay petsitter 80


### INPUT
"""
Always updating salary or hours can get tedious and prone to error. 
A dynamic way to solve this is input()
This is like a prompt
Have you ever had to input something into a blank space that is a prompt
like Username: and Password:
input() makes user inputs allowed. 

you can take user input and load it into a variable like this
username = input()
password = input()

However, you might need a bit more. 
if you run input() the console or interpreter will just sit there and and wait
for user input before going any further. input() will give no instruction and
look like nothing has happened. we need to show some instruction to the user. 
"""
username = input() # you will need to type something in your console and hit enter
print(username)
#verses

username = input("Enter username: ") #enter a name in the console and hit Enter

print(username)
"""
Converting input types
input will think no matter what that whatever you enter is a string. 
At some point you will enter numbers into the input
but input will automatically change this to a string. int() will help
this is a way to convert a string to an integer(within reason).
"""
int( )
str()
float()

hours = '40'
wage = 20

hours = int(hours)

hours * wage # what just happened? Might be useful later.

int(hours) * wage


"""Let's convert an input into an integer"""

wage = int(input("Enter wage :$"))
hours = int(input("Enter hours worked:"))
#finish the code enter a prompt asking for number of weeks worked
weeks = int(input("Enter number of weeks worked:"))

print('Salary is', wage * hours * weeks)


## EXERCISE
"""
Rebuild the Tip Calculator with dyanmic inputs
hint. one input will give an error because it is a float not an int

Bonus: Once you have the script working copy it and past it into its own script
save it as tipcalc in your pythonscripts folder and try running it from cmd
"""

bill = int(input("Enter the bill amount:$"))
tip = int(input("Enter the tip percentage:%"))

# the final bill is calculated as the bill plus the tip as a percentage of the bill amount
final_bill = round(bill * (1 + (tip / 100)))
print("Your final bill is :$", final_bill)

input("click enter to exit")


###############################################################################
##                            ERRORS                                         ##
###############################################################################
#TYPES OF RUNTIME ERRORS
#Error type 	  Description
#SyntaxError 	  The program contains invalid code that cannot be understood.
#IndentationError The lines of the program are not properly indented.
#ValueError 	  invalid value is used – can occur if giving letters to int().
#NameError 	      The program tries to use a variable that does not exist.
#TypeError 	      An operation uses incorrect types – can occur if adding an 
                  #integer to a string.
"""
Logical errors known as bugs

A good example is needing to mark items up by 2% and creating a calc of .2
instead of .02

Another one is when working with time many people forget about leap year for
doing trend analysis. or comparing this year, last year.
"""
###############################################################################
##                             STRINGS                                       ##
###############################################################################
''' If you have ever done any amount of working with SQL or EXCEL you will be 
familiar with the need to review and manipulate strings or data in cells.

Strings and string literals
string literal created by single or double quotes, such as 'Cat' or "Cat".

A character's position is called the character's index, starts at 0. 
| C | a | t |
| 0 | 1 | 2 |

you can get a character at a specific index by using
brackets [ ] containing the index: 
'''
   
pet = 'Cat'
print(pet[0])
print(pet[0], pet[1], pet[2])# complete this to bring back "t"
print(pet[0:2])

# slicing
po = "110010125001" #locId 3 digits | Date 6 digits | Seq 3 digits
print(po[0:3])      # on your second loop take out the quotes and solve
loc = po[0:3]

seq = po[9:12]
print("The location is", loc)



# slicing
po[-1]       # returns end of the string
print(po[-3:])
seq = po[-3:]        # finish the code
print("The sequence is", seq)        # finish the code to behave like the loc print statement

## EXERCISE SLICE THE DATA
# Expected outcom 010125
dates = po[3:9]
print("The date is", dates)

# concatenating concats are the same as Excel or SQL you can concat blanks or multiple columns
pets = "cat"
pets = pets + "dog"
print(pets)        # use plus sign to combine strings
print(pets, "burrito") # comma is a good way to combine elements but not a concat


string_1 = 'abc'
string_2 = '123'
concat = string_1 + string_2
print('Easy as ' + concat)

# concatenating ()
str(5) + ' there'   # cast 5 to a string str() in order for this to work

### EXERCISE ###
"""
Add your city and state
Assign log_entry with current_time, my_city, and my_state. 
Sample output for given program 
2014-07-26 02:12:18: Houston Texas

#hint concat or combine was not used in requirements
"""
current_time = '2014-07-26 02:12:18:'
my_city = "Bukit Panjang"
my_state = "Singapore"
log_entry = ''' Your solution goes here '''

# AG --> Not sure how this can be done without combine or concat?! 
print(log_entry)


"""
String values cannot change(immutable). An assignment statement must be used to 
update an entire string variable.
"""
# Change to upper case
alphabet = 'abcdefghijklmnopqrstuvwxyz'
alphabet[0] = 'A'  # Invalid: Cannot change character
alphabet[1] = 'B'  # Invalid: Cannot change character
print('Alphabet:', alphabet)

# solution st
alphabet = 'abcdefghijklmnopqrstuvwxyz'

# Change to upper case
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
print('Alphabet:', alphabet)

# uppercasing
state = "washington"
state = state.upper()       # string method (this method doesn't exist for lists)
print(state)
state = state.title()
print(state)

## EXERCISE USE slicing and string functions to bring state back as WA

'''your solution here'''
state = "washington"
short_state = state[:2].upper()
print(short_state)


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
dates = po[3:5] + "/" + po[5:7] + "/" + po[7:9]
seq = po[-3:]
print(f"Loc:{loc}",f"Date: {dates}",f"Seq:{seq}")


"""
String length and indexing
The len() built-in function can be used to find the length of a string .
The \ character after the string literal extends the string to the following 
line.
"""
country = 'United States'
state = "WA"
city = 'Seattle'

print(len(country), 'country name length')
print(len(state), 'state name length')
print(len(city), 'city name length.')


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

print("I have %d %r and %d %r"%(c,b,c,a))

"""
#A 'Mad Libs' style game where user enters nouns,
#verbs, etc., and then a story using those words is output.
"""

### EXERCISE FIX THE CODE
#Get user's words
relative = input('Enter a type of relative: ')
food = input('Enter a type of food: ')
adjective = input('Enter an adjective: ')
period = input('Enter a time period: ')

# Tell the story
print('My', relative, 'says eating', food)
print('will make me more', adjective)
print('so now I eat it every', period)



# Using format to accomplish the same task
a = 'cats'
b = 'dogs'
c = 5
("I have {} {} and {} {}").format(c,b,c,a)

x = "fun"
print("Mad_libs is a {} game".format(x))

##Example 2
print("Mad_libs is a {0} {1}.".format("fun","game"))


# variables often times are loaded into variables
x = "fun"
y = "dog"
print("Mad_libs is a {} game. I like to play with my {}.".format(x,y))


x = "fun"
y = "dog"
z = "Mad_libs is a {} game. I like to play with my {}.".format(x,y)
print (z)

''' Now you can make a mad libs game in a seperate script and call it like 
a program!'''



''' PROJECT EXERCISE - REVIEW 
Open a new script called and name it PythonSkillBuilder
Make a list of skills and score it. 

0 = Don't know
1 = Aquiring knowledge
2 = Can apply with < 80% help from Google
3 = Can apply with < 20% help from Google
4 = Can teach < 20% help from Google
5 = Can design, review, optimize < 20% help from Google

1) Create Variables that will hold each rating score
2) Review what has been covered
3) Print a line for each skill you have learned and rate it by passing variable in
    z= "printing        : {}".format(a)

What areas are you doing great in, what areas do you need to study?
This Project will grow and be designed and redesigned several different ways
as you progress and revist. You can take step 3 from above and make it a dynamic
input. This is your area to create and develop your own program. 

When you have completed the course come back to this lesson
and update it. Think about the new things you have learned and how you can modify your 
first block of code.

As your coding, if you think,"There has to be an easier way!" There usually is.  
Take notes on any ideas or thoughts," Can I do an average score?". "How?" '''