rooms = {
        'Dining room': 'where the murder happened',
        'Back door': {'well': 'poison bottle'},
        'Lilian\'s bedroom': {'bedside table': 'little key'},
        'Lilian\'s office': {'fireplace': 'note', 'safe': 'bronze key'},
        'Jay\'s bedroom': {'coat hanger': 'recipt'},
        'Megan\'s bedroom': {'under the bed': 'notebook'},
        'Abriella\'s bedroom': 'nothing to be found'
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
    if room_choice == 'dining room':
        print(f"The Dining room is where the murder happened.")
    # if room choice is abriella's bedroom
    elif room_choice == "abriella's bedroom":
        print(f"There is nothing in Abriella's room.")
    # if room choice is back door
    elif room_choice == 'back door':
        print("The door is locked.")
        item_choice = input(f"Use an item to open the door:")
        if item_choice == 'bronze key':
            print(f"There is a well, with a rope and nothing to pull up the water.")
            item_choice = input(f"Use an item to pull up the water:")
            if item_choice == 'bucket':
                print(f"You found a bottle with poison.")
            else:
                print("That is the wrong item.")
        else:
            print("That is the wrong item.")
    # if room choice is lilian's office
    elif room_choice == "lilian's office":
        print("The door is locked.")
        item_choice = input(f"Use an item to open the door:")
        if item_choice == 'golden key':
            print(f"There is a fireplace and a safe.")
        else:
            print("That is the wrong item.")
    elif room_choice == "lilian's bedroom":
        print("The door is locked.")
        item_choice = input(f"Use an item to open the door:")
        if item_choice == 'silver key':
            print(f"There is a bedside table.")
            print("")
        else:
            print(f"{place_choice} is not an option.")


    else:
        print(f"{room_choice} is not one of the choices.")
else:
    print(f"{choice.title()} is not one of the choices.")


        # for place, object in find.items():
        #     print(f"In {room}, there is {place}, where you can find {object}.")
    #     else:
    #         for where, thing in find.items():
    #             print(f"In {room}, there is {where}, where you can find {thing}.")
