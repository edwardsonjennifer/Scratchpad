if __name__ == "__main__":
    # Another storage container similar to lists and tuples.
    # Values are as key:value pairs.
    # Are created using the curly brackets or dict constructor.
    # Dictionaries are mutable.
    # Dictionary keys MUST be immutable (int, float, str, bool, tuple).
    # Order is NOT guaranteed (especially older Python versions)

    # pokemon_types = {
    #     # Key    :  Value
    #     'Pikachu': 'electric',
    #     'Bulbasaur': 'grass, poison', 
    #     'Charmander': 'fire'
    # }

    # print(pokemon_types)

    # pokemon_types_pair = (
    #     ('Pikachu', 'electric'), 
    #     ('Bulbasaur', 'grass, poison'),
    #     ('Charmander', 'fire')
    # )

    # pokemon_types_from_tuple = dict(pokemon_types_pair)
    # print(pokemon_types_from_tuple)

    # print(pokemon_types['Pikachu'])
    # print(pokemon_types.get('Pikachu'))

    # print('Mew' in pokemon_types)
    # print(pokemon_types.get('Mew', 'Unknown'))

    # pokemon_types['Mew'] = 'psychic'
    # pokemon_types['Squirtel'] = 'water'
    # print(pokemon_types)

    # del pokemon_types['Squirtel']
    # print(pokemon_types)

    # pokemon_types['Squirtle'] = 'water'
    # print(pokemon_types)

    # for key, value in pokemon_types.items():
    #     print(f'Pokemon {key} is of type {value}.')

    pokedex = {
        25 : {
            'name': 'Pikachu',
            'type': 'electric'
        },
        1 : {
            'name': 'Bulbasaur',
            'type': 'grass, poison'
        },
        4 : {
            'name': 'Charmander',
            'type': 'fire'
        }
    }
    
    # indexing into dictionaries, you can do this with lists as well
    print(pokedex)
    print(pokedex[25]['name'])
