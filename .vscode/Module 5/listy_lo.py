if __name__ == "__main__":
    food = ['rice', 'beans']
    print(food)

    food.append('broccoli')
    print(food)

    food.extend(['bread', 'pizza'])
    print(food)

    print(food[len(food) - 1])

    morning = ('eggs, fruit, orange juice')
    breakfast = morning.split(',')
    print(breakfast)
    print(len(breakfast))
 
    numlist = []
    while True:
        inp = input('Enter an number(type "stop" to end): ')
        if inp == 'stop':
            break
        value = float(inp)
        numlist.append(value)

    fl_avg = sum(numlist) / len(numlist)
    print(f'Average: {fl_avg}, Min: {min(numlist)}, Max: {max(numlist)}')
