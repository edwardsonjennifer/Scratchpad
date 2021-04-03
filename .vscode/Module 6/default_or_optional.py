# what if, we wanted to have the ablity to change tax rate?
# but still have the default be 0.10
def calculate_weeks_pay(hours = 30, pay = 15.25, tax_rate=0.10, **kwargs):
    print(kwargs)
    gross = hours * pay
    net_rate = 1 - tax_rate
    # tax_rate 10%
    net = gross * net_rate
    return net, gross

# print(calculate_weeks_pay(30, 15.25, tax_rate=0.05))

weekly_pay = (30, 15)
hours, pay = weekly_pay

# print(calculate_weeks_pay(hours, pay))
# print(calculate_weeks_pay(*weekly_pay, tax_rate=0.15)) # the * unpacks the tuple

weeks_summary = {
    'hours': 25,
    'pay': 16.00,
    'tax_rate': 0.10,
    'week_number': 26,
    'year': 2019
}

# calculate_weeks_pay(hours=weeks_summary['hours'], pay=weeks_summary['pay'], tax_rate=weeks_summary['tax_rate'])
print(calculate_weeks_pay(**weeks_summary))