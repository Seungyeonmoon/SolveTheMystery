rooms = {
        'Dining room': 'where the murder happened',
        'Kitchen': {'cabinet': 'golden key',
                    'stove': 'cattle',
                    'pantry': 'bucket on the floor',
                    'sink', 'turn on water tap'
                    },
        'Back door': {'well': 'poison bottle'},
        'Lilian\'s room': {'bedside table': 'little key'},
        'Lilian\'s office': {'fireplace': 'note', 'safe': 'bronze key'},
        'Jay\'s room': {'coat hanger': 'recipt'},
        'Megan\'s room': {'under the bed': 'notebook'},
        'Abriella\'s room': 'nothing to be found'
        }

inventory = ['notebook']

actions = ['check inventory', 'explore rooms']

print(f"\nWhat would you like to do?")
for action in actions:
    print(f"\t* {action.upper()}")
choice = input(f"")
# when user types in check inventory
if choice == 'check inventory':
    for items in inventory:
        # print list of items
        print(f"\t*{items.upper()}")
# when user types in explore rooms
elif choice == 'explore rooms':
    print("Which room would you like to explore?")
    for room in rooms.keys():
        # print list of rooms
        print(f"\t* {room.upper()}")
    room_choice = input(f"")
    # if room choice is dining room
    if room_choice == 'dining room':
        print(f"The Dining room is where the murder happened.")
    # if room choice is kitchen
    elif room_choice == 'kitchen':
        print("There is a pantry.")
    # if room choice is back door
    elif room_choice == 'back door':
        print("The door is locked.")
    # if room choice is lilian's office
    elif room_choice == "lilian's office":
        print("The door is locked.")
    # if room choice is Lilian's room
    elif room_choice == "lilian's room":
        print("The door is locked.")
    # if room choice is Megan's room
    elif room_choice == "megan's room":
        print("There is a notebook under the bed.")
    # if room choice is Jay's room
    elif room_choice == "jay's room":
        print("There is a coat on a coat hanger")
    # if room choice is abriella's room
    elif room_choice == "abriella's room":
        print(f"There is nothing in Abriella's room.")
    else:
        print(f"{room_choice} is not one of the options.")

else:
    print(f"{choice.title()} is not one of the choices.")
