if __name__ == "__main__":

    pokemon = ('picachu', 'charmander', 'balbasaur')
    starter1, starter2, starter3 = pokemon

    print(pokemon[1])

    print(pokemon)
    print(starter1)
    print(starter2)
    print(starter3)

    first_name = tuple('Jennifer Edwardson')
    print('i' in first_name)

    for i in range(2, 11):
        print(i)

    numbers = range(2, 11)
    i = 0
    while i < len(numbers):
        print(numbers[i])
        i += 1

    simple_str = 'This is a simple string'

    for letter in simple_str:
        print(letter)

    simple_tuple = ('this', 'is', 'a', 'simple', 'set')
    j = range(0, len(simple_tuple))
    for letter in range(5):
        for j in range(0, 3):
            print(simple_tuple[letter])

