# check to see if A is in between 0 and 20
A = -10
B = 0

# print(A % 2 == 0 and (not B % 2 == 0))

# False == (not True) will output true because the not True is calculated first
# than the False == False (which is True)

print(A >= 0 and (A / B) > 0)

# you have to be careful. This will evaluate the first statement
# and output False without raising a ZeroDivisionError for the second statement
