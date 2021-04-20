def print_comparisions(A, B):
    print(f'{A} >  {B}: {A >  B}')
    print(f'{A} <  {B}: {A <  B}')
    print(f'{A} >= {B}: {A >= B}')
    print(f'{A} <= {B}: {A <= B}')
    print(f'{A} == {B}: {A == B}')
    print(f'{A} != {B}: {A != B}')

A = 'apples'
B = 'applesauce'

print_comparisions(A, B)

print('A ord : B ord')
for a_char, b_char in zip(A, B):
    print(f'{ord(a_char):<6}: {ord(b_char):>}') 
    
    # the <6 means that it fills 6 character with left align
    # the > means right align
    # the string that is larger will be the greater value