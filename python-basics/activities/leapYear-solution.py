# solution for leapYear.py

# assign a year to a variable
year = 2004
# assign the boolean to variable, and set its default
isLeapYearBool = False
# use modulus to check the remainder
remainder = year % 4

# this is where you do the checking
if remainder == 0:
    # if it fits this criteria, change the boolean variable
    isLeapYearBool == True

# print this to console / terminal
print(isLeapYearBool)