
# pass by referance, list are mutable and can be changed

students = ['james', 'joe', 'sally']

print(students)

def append_sue_to_list(my_list):
    my_list.append('sue')

append_sue_to_list(students)

print(students)