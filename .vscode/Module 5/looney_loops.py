
if __name__ == '__main__':

    vowels = ('a', 'e', 'i', 'o', 'u')

    # i = 0
    # # as long as condition is true it will continue to loop, can be used for unknown lenght of loops or continuous looping (good for tracking movement(cursor))
    # while i < len(vowels):
    #     print(vowels[i])
    #     i += 1 # This is equal to i = i + 1

    # for letter in vowels: # great for finite(it will end) and you know it will end loops
    #     print(letter)

    # # stops at range(#) but does not print it, ex. range(10) will print 0-9, range(10, 20) will print 10-19
    # for i in range(10, 20, 2): # (start, stop, step) this ex. will print even #s
    #     print(i)

    for i in range(5):
        print('pre-nested loop')
        for j in range(5, 8):
            print(f'i = {i}; j = {j}')
        
        print('post-nested loop')

    print('script complete')