if __name__ == "__main__":

    # my_tuple = (1, '2.0', 3.0, (4, 5))
    # print(my_tuple)

    # # indexing into the tuple above my_tuple
    # print(my_tuple[0])
    # print(my_tuple[1])
    # print(my_tuple[2])
    # print(my_tuple[3])

    # immutable - they DO NOT change unless you re-declare/reassign
    hello = 'Hello There'
    my_tuple = tuple(hello)
    print(my_tuple)

    # quary = (4, 5) # will check if other variable are in variables
    # print(f'"{quary}" is in my tuple?: {quary in my_tuple}') # Will print true/false

    for letter in my_tuple:
        print(letter)

    print('script complete')