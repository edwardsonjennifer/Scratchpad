# print('This is the start of the file.')

# if I call the function here before it has been defined it will create a error.
# it will have a NameError

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
    return net_pay, gross_pay

# print('Calling the function.')
net_pay, gross_pay = calculate_weeks_pay(34.5, 16.25)

print(f'Your net pay is ${net_pay:.2f}')
print(f'Your gross pay is ${gross_pay:.2f}') 
# print('End')