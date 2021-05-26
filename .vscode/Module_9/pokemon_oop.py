caterpie = ['caterpie', 13, 40, ('String Shot', 10)]

print (caterpie[0])

caterpie = {
    'name': 'caterpie',
    'level': 13,
    'hp': 40,
    'move': ('String Shot', 10)
}
### Module 9.1 Notes
## What is OOP?
# sometimes code can repetitive or weird, wanting a neat and clean code
# it gives you the ability to distile a massive amount of code into a section

## OOP is a paradigm
# using objects to represent specific elements within a program
# objects have data, functions, etc. OOP allows us to hide complexity
# good philosiphy is to break down code to it's smallest elements and breach out from there

## OOP is not new
# all the way back to 1950 to 1960. Simula was in the early 1970
# Today, we have programs that are built around OOP (Python, Java, C#)
# and implemented aspects of OOP (PHP, Perl, or Matlab)

## OOP has 4 concepts
# -Encapsulation - the processd of encapsulating, or organizing code so that only the relevant
# parts are available to the user.
# -Abstraction - the process of abstracting, or templating code to show the basic requirements
# a specific set of code should accomplish. 
# -Inheritance - the process of inheriting, or reusing code with little to no changes in between
# objects.
# -Polymorphism - the concept that one thing, a class, can be used to decribe multiple different
# things even though the details may be different for each.

# An object like Pokemon Cards can have similar attributes (name, hp, type, move(s), weakness)
# Pokemon can be thought as a class of monsters. One specific pokemon can be a object or instance
# of the class Pokemon. 
# 
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
# str, int and other data types are instances of objects
# you can access a objects "directory" or available attributes and methods via the dir function
#
## Everything in Python is a object
# This includes the variables, functions, ##