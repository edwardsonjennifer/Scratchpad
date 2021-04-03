# print('This is the start of the file.')

# if I call the function here before it has been defined it will create a error.
# it will have a NameError

# !!!this is Pass by Value bc tuples are immutable and cannot be changed.
# Therefore, it is passing by the defined value of the variables

DEFAULT_HOURS = 30.0
DEFAULT_PAY = 15.25

print(id(DEFAULT_HOURS))

def calculate_weeks_pay(hours, hourly_pay):
    '''calculates the weeks pay
    Assume that a 10% of the gross pay will be taken for payment of taxes.
    Parameters:
    -----------
    hours : float
        the number of hours worked for the week
    hourly_pay : float
        the hourly payment

    Returns
    ------------
    float 
        the net pay expected'''
    # print('This is the start of our function.')
    gross_pay = hours * hourly_pay
    net_pay = gross_pay * 0.90
    return net_pay, gross_pay # creates a tuple!!!

net_pay, gross_pay = calculate_weeks_pay(34.5, 16.25)

print(f'Your net pay is ${net_pay:.2f}') # These are defined by the above called function
print(f'Your gross pay is ${gross_pay:.2f}') 

print(calculate_weeks_pay(DEFAULT_HOURS, DEFAULT_PAY)) # these are defined by the DEFAULT values above
