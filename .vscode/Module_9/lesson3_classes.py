### Object Factories using Classes
# Classes are similar to factories where you can stamp out similar objects 
# with similar attributes.
# 
## Creating Custom Classes
# similar to function. Should us Camelcase or Caplitize the first letter in every word
# Ex. This_Is_A_Class_Name
# Format: 
# class <name> (<parent class>):
# the next line is indented and the body defines the class. 
# 
# For defining a method, you must use 'self' as the first variable 
# and indent one level under the class definition.
# Format: 
# def <name> (self, <variables>):

# class Pokemon():
#     generation = 1
#     def print_choice(self, pokemon_name):
#         print(f"I choose you {pokemon_name}!")

# poke = Pokemon()

# poke.print_choice('pikachu')
# print(poke.generation)

# notice that to call an object function, there's no passing the first
# var of self to it.  This is done automatically by Python in the 
# background. Outputs I choose you pikachu! and 1 for the pokemon generation

## Dunder Methods 
# dunder(double underscore __ ) methods are special methods (called magic methods) that have
# specific meaning when defining a class.
# 
# __init__ is the initialization of an object. Most important dunder.
# __str__ is what the object should be when 'printed' or converted to a string.##

# class Pokemon():
#     generation = 1 # This is a class attribute
    
#     def __init__(self, name, level): # self references to the current object
#         self.name = name # This is a instance attribute
#         self.level = level
        
#     def print_choice(self):
#         print(f"I choose you {self.name}!")
        
#     def __str__(self):
#         return f"Pokemon: {self.name}"

# pikachu = Pokemon('pickachu', 10)
# bulbasaur = Pokemon('bulbasaur', 12)

# pikachu.print_choice()
# # I choose you pickachu! : this is calling the def print_choice so variable.method()

# print(bulbasaur)
# # Pokemon: bulbasaur : this is calling the def __str__ method

## Class and Instance Basics 
# Class attributes are always available for all instances(unless changed by the instance) and
# for the class itself
# Instance attributes are available for only the instance
# Use class attributes/methods only if it's intended to be instance independent. The attribute 
# can be the same for ALL instances.#

class Pokemon():
    generation = 'Base'
    
    def __init__(self, name, level, start_hp, energy_type, moves, weakness, resistance):
        self.name = name
        self.level = level
        self.hp = start_hp
        self.energy_type = energy_type
        self.moves = moves
        self.weakness = weakness
        self.resistance = resistance

    def take_damage(self, damage_amount):
        self.hp = self.hp - damage_amount

    def has_move(self, moveset):
        print(self.moves[0] == moveset)
        
    def __str__(self):
        return f'Pokemon: {self.name} at level {self.level} with {self.hp} HP left'
    
# print (Pokemon.generation) # Base : this is just calling the class attribute.

koffing = Pokemon('Koffing', 13, 60, 'psychic', ('Foul Gas', 10), 'psychic', 'None')
poliwag = Pokemon('Poliwag', 13, 60, 'water', ('Water Gun', 30), 'grass', 'None')
starmie = Pokemon('Starmie', 28, 90, 'water', ('Star Freeze', 30), 'grass', 'None')
sawsbuck = Pokemon('Sawsbuck', 29, 90, 'grass', ('Nature Power', 20), 'fire', 'water')

def battle(poke1, poke2):
    while poke1.hp > 0 and poke2.hp > 0:
        if poke1.energy_type == poke2.resistance: # for resistance
            poke2.take_damage(poke1.moves[1] - 20)
        elif poke1.energy_type == poke2.weakness: # for weakness
            poke2.take_damage(poke1.moves[1] * 2)
        else:
             poke2.take_damage(poke1.moves[1])    # for normal damage

        if poke2.energy_type == poke1.resistance:
            poke1.take_damage(poke2.moves[1] - 20)
        elif poke2.energy_type == poke1.weakness:
            poke1.take_damage(poke2.moves[1] * 2)
        else:
            poke1.take_damage(poke2.moves[1])
        

    print(poke1)
    print(poke2)

battle(starmie, sawsbuck)

koffing.has_move('Foul Gas')