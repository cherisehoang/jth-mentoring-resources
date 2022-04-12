# if, else, and elif

# sometimes, we will want a program to do certain things if a certain criteria is met.

# firstly, how do we compare two different things?
# equals: a == b
# not equals: a != b
a, b = 100, 200 # assigning values to variables
a == 100
a != 200
b != a
# we can also do basic maths operations to compare two numbers
# less than: a < b
# less than or equal to: a <= b
# greater than: a > b
# greater than or equal to: a >= b
a < b
a <= b
b > a
b >= a

# now we can start making the program do things when certain things compared to each other are true or false
# i.e. when certain conditions are met.
# we can do this with if statements!
if a > b: 
    print("a is greater than b")
# here, we are asking the program to check if a is greater than b. if it is greater than b, print line 25.
# note that I indented line 25, this is important! Python loves indentation, or else it won't work.

# what if we need the program to do two (or more) different things for two (or more) different conditions?
# two options:
# we use 'else' if no other previous conditions are met:
if a > b:
    print("a is greater than b")
else:
    print("b is greater than a")
# we use 'elif' as shorthand for 'else if', where if the current previous conditions are not met:
if a > b:
    print("a is greater than b")
elif a == b:
    print("a is equal to b")
# we can use both elif and else:
if a > b:
    print("a is greater than b")
elif a == b:
    print("a is equal to b")
else:
    print("this only happens if lines 43 and 45 are both false")


# shorthand if:
if a > b: print("a is greater than b")
# shorthand if-else:
print("a is greater than b") if a > b else print("a is not greater than b")


# want to combine two statements into one? you can!
# and: check if two statements are satisfied at the same time
# or: check if at least one statement of the two is true
if a < b and a != b:
    print("Both conditions are true")
elif b > a or b != a:
    print("One of these two conditions are true")


# want the program to check again for something else if the first condition was true?
if a < b:
    print("a is less than b")
    if a >= 100:
        print("a is less than b and ALSO greater than or equal to 100")
    else:
        print("a is less than b but NOT greater than or equal to 100")
    # these are called nested if-else statements
else:
    print("a is not less than b")
