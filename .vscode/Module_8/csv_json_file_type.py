import csv
        #encoding helps when you export a file from another location
# with open('01resources/pokemon_sm.csv', encoding='utf-8-sig') as reader:
#     csv_reader = csv.reader(reader)
#     for row in csv_reader:
#         print(row)

with open('01resources/pokemon_sm.csv', encoding='utf-8-sig') as reader:
    csv_reader = csv.DictReader(reader)
    for row in csv_reader:
        print(f"Pokemon with ID: {row['num']} is called {row['pokemon']} and is the {row['type']} type.")