### Module 9.2 Notes
## Understanding Objects
# Objects are a constructed instance of a class that contains all the attributes and methods that
# were defined by the class. Also called a instance.
# Objects have:
# -Attributes(properties): class variables that store data.
# -Methods: class functions for processing data. 
# -attributes and methods are accessed via the 'dot' notation.
# -Can be assigned to variables and passed into functions.
# 
## dir Keyword
# str, int and other data types are instances of objects
# you can access a objects "directory" or available attributes and methods via the "dir" function
#
## Everything in Python is a object
# This includes the variables and functions

# def simple_func(var1, var2 = 2):
#     out = f'{var1}' * var2
#     print(out)
#     return out

# simple_func('stutter', 3) 

# you can assign a function itself(not its output) to a variable
# my_var = simple_func
# my_var('stutter')

# we can pass the function into another function to be used. A function calling a function.
# def func_caller(func):
#     func('stutter')

# func_caller(simple_func) # outputs stutterstutter
# func_caller(print) # outputs stutter
# 
## Object Type and Creation
# all objects have a type associated to it. Like 12 is a int and 'one' is a str and 
# func_caller is a function
# 
## Object Lifecycle
# Definition: A class defines how an object will be created.
# Initialization: An object is created through the class instantiation.
# Access and Manipulation: The object is being used within the programe.
# Destruction:The object is dereferenced or no longer used and flagged
# for deallocation. The object is no longer in memory.
# 
# Using dir, determine the number of non-dunder attributes/methods for a dict class. 
# Bonus points if you do this programmatically.##

test = {} # this is a empty dictionary
count = 0 # starting count
for item in dir(test): # for a item in the directory of test(a dictionary)
    if item.startswith('__'): # if the item starts with the dunder '__'
        continue # continues pass any item the returns true in the if statement
    count += 1 # counts one for every item in the for statement that is not in the if statement
print(count) # Lastly, prints the count of non-dunder attributes of the dictionary