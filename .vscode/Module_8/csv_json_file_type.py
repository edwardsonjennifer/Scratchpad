import csv
import json
        #encoding helps when you export a file from another location
# with open('01resources/pokemon_sm.csv', encoding='utf-8-sig') as reader:
#     csv_reader = csv.reader(reader)
#     for row in csv_reader:
#         print(row)

# with open('01resources/pokemon_sm.csv', encoding='utf-8-sig') as reader:
#     csv_reader = csv.DictReader(reader)
#     for row in csv_reader:
#         print(f"Pokemon with ID: {row['num']} is called {row['pokemon']} and is the {row['type']} type.")

with open('01resources\pokemon_sm.json') as reader:
    pokemon = json.load(reader) #.load is reading the .json file

#print(pokemon) #This will create a dictionary or list of dictionaries
    
for monster in pokemon:
    print(f"Pokemon with ID: {monster['id']} is called {monster['name']} and is the {monster['type']} type.")