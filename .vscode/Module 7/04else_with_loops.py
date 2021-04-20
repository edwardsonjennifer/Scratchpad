# fruits = 'apples cherries blueberries blackberries'.split()

# for fruit in fruits:
#     if 'peach' in fruit:
#         break
#     print(fruit)
# else:
#     print("peach wasn't found in the fruits")

max_guesses = 3
num_guess = 0
val_check = 'jennifer'

while num_guess < max_guesses:
    val = input('Enter your guess: ')
    if val == val_check:
        print('You won! :D')
        break

    num_guess += 1
else:
    print('You lose :(')

print('Game Over!')
