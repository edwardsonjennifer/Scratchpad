

if __name__ == "__main__":

    # # lists are mutable which means the place order and values can change
    # colors = ['red', 'yellow', 'blue', 'green']
    # print(colors)
    # print(type(colors))

    # hello_list = list('hello there')
    # print(hello_list)

    # # tuples use (), while list use []
    # my_tuple = (1, 2, 3)
    # print(my_tuple)
    # my_list = list(my_tuple)
    # print(my_list)

    # # use element (elem) 
    # for elem in my_list:
    #     print(elem)

    # colors[0] = 'cyan'
    # print(colors)

    # # Sort by character value so Uppercase goes before lowercase
    # colors.sort()
    # print(colors)

    # # Cannot do mixtures of str and int
    # my_list = [1, 'one', 2, 'two']
    # my_list.sort()
    # print(my_list)

    # # .append adds a value to the list
    # colors.append('red')
    # print(colors)

    # numbers = []
    # for i in range(5):
    #     numbers.append(i ** 2)

    # print(numbers)

    # # .pop takes away a value from a list
    # num = numbers.pop()
    # print(num)
    # print(numbers)


    # first = list(range(5))
    # second = list(range(5, 10))
    # combined = first + second
    # # print(first)
    # # print(second)
    # # print(combined)

    # # print(combined[2:7]) # can do a range of numbers

    # print(max(combined))
    # print(min(combined))
    # print(sum(combined))

    # # this is equivalent to print(sum(combined))
    # total = 0
    # for i in combined:
    #     total += i

    # print(total)

    # DO NOT add spacing it will print FALSE
    pokemon = 'pikachu,bulbasaur,charmander'
    my_pokemon = pokemon.split(',')
    print(my_pokemon)

    # print('bulbasaur' in my_pokemon)

    # use [:] to seperate the two variables
    pokedex = my_pokemon[:]
    print(pokedex)
    print(my_pokemon)

    pokedex.append('mew')

    print(pokedex)
    print(my_pokemon)

    print('script complete')
