if __name__ == "__main__":

    pokedex = dict()

    pokedex['Venosaur'] = ['Grass', 'Poison']
    pokedex['Charizard'] = ['Fire', 'Flying']
    pokedex['Blastoise'] = ['Water']

    print(pokedex)

    del pokedex['Blastoise']

    print(pokedex)