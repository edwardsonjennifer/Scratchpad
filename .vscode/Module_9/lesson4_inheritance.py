### Inheritance is like Genetics
# Similar to genes, classes in Python can inhert from other classes.
# Classes that pass on "genes" (attributes/methods) are called parents
# Classes that recieve the "genes" (attributes/methods) are called children
# 
# Parent Class: a class that is used to contribute all it's attributes and methods to a child class.
# The parent class will give every one of its attributes and methods to the child unlike genetics.

# Child Class: a class that is used to extend another parent class by inheriting all 
# the parents attributes and methods.#

class Pokemon():
    generation = 'Base'
    
    def __init__(self, name, level, start_hp, energy_type, moves):
        self.name = name
        self.level = level
        self.hp = start_hp
        self.energy_type = energy_type
        self.moves = moves
        
    def __str__(self):
        return f'Pokemon: {self.name} with {self.hp} HP left'

    
def print_non_dunder(obj):
    for item in dir(obj):
        if not item.startswith('__'):
            print(item)

# print_non_dunder(Pokemon('Starmie', 28, 90, 'water', [('Star Freeze', 30)]))

# class SubPokemon(Pokemon):
#     pass
# print_non_dunder(SubPokemon('Starmie', 28, 90, 'water', [('Star Freeze', 30)]))

## Using 'super' to Extend Parent Classes
# 'super' is another function that is used to take a Parent's attribute/method. It enables
# developers to call and overridden method such a __init__.#


# class WaterPokemon(Pokemon):
#     def __init__(self, name, level, start_hp, moves):  # Notice that energy types isn't here
#         super().__init__(name, level, start_hp, 'water', moves)
#         self.weakness = 'electric'
        
class GrassPokemon(Pokemon):
    def __init__(self, name, level, start_hp, moves):
        super().__init__(name, level, start_hp, 'grass', moves)
        self.weakness = 'fire'

# starmie = WaterPokemon('starmie', 28, 90, [('Star Freeze', 30)])
# print(starmie.energy_type)

class WaterPokemon(Pokemon):
    def __init__(self, name, level, start_hp, moves,):
        super().__init__(name, level, start_hp, 'water', moves)
        self.weakness = 'electric'
        # call the super first so if needed you can make changes after
        # the variable is called.

poliwag = WaterPokemon('Poliwag', 13, 60, ('Water Gun', 30))
starmie = WaterPokemon('Starmie', 28, 90, ('Star Freeze', 30))
caterpie = GrassPokemon('caterpie', 13, 40, [('String Shot', 10)])

print(caterpie.energy_type)
print(poliwag.energy_type)