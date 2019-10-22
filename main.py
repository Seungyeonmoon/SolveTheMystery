# Seungyeon Moon
# CS30 P.1
# Oct.25/2019
# main file for the game

# list of rooms and the items that you can find
rooms = {
        'Dining room': 'where the murder happened',
        'Back door': {'well': 'poison bottle'},
        'Lilian\'s bedroom': {'bedside table': 'little key'},
        'Lilian\'s office': {'fireplace': 'note', 'safe': 'bronze key'},
        'Jay\'s bedroom': {'coat hanger': 'recipt'},
        'Megan\'s bedroom': {'under the bed': 'notebook'},
        'Abriella\'s bedroom': 'nothing to be found'
        }
for room, find in rooms.items():
    if room == 'Dining room':
        print(f"{room} is {find}.")
    elif room == 'Abriella\'s bedroom':
        print(f"There is {find} in {room}.")
    else:
        for where, thing in find.items():
            print(f"In {room}, there is {where}, where you can find {thing}.")

print("")

# List of characters in the game with their age and illness
characters = {
             'Lilian': {'age': 'in her 60s', 'illness': 'heart problems'},
             'Jay': {'age': 'in his 30s', 'illness': 'high blood pressure'},
             'Megan': {'age': 'in her 30s', 'illness': 'no illness'},
             'Abriella': {'age': 'in her 20s', 'illness': 'asthma'}
             }
for person, description in characters.items():
    print(f"{person}:")
    age = f"{description['age']}"
    illness = f"{description['illness']}"
    print(f"\t{person} is {age}.")
    print(f"\t{person} has {illness}.")

print("")

# items that need to be found to countinue the game
missing_items = {
                'Lilian\'s office': 'golden key',
                'Lilian\'s bedroom': 'silver key',
                'back door': 'bronze key',
                'cabinet': 'little key',
                'well': 'bucket',
                'fire': 'kettle with water',
                'information': 'notebook'
                }
for place, items in missing_items.items():
    print(f"You need to find {items} for {place}.")
