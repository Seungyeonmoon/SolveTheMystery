rooms = {
        "dining room": 'where the murder happened',
        "kitchen": {'cabinet': 'golden key',
                    'stove': 'cattle',
                    'pantry': 'bucket on the floor',
                    'sink': 'turn on water tap'
                    },
        "back door": {'well': 'poison bottle'},
        "Lilian's room": {'bedside table': 'little key'},
        "Lilian's office": {'fireplace': 'note', 'safe': 'bronze key'},
        "Jay's room": {'coat hanger': 'recipt'},
        "Megan's room": {'under the bed': 'notebook'},
        "Abriella's room": 'nothing to be found'
        }

inventory = ['notebook']


def play():
    """looping through the game"""
    # directions & actions
    action = ['explore rooms', 'check inventory', 'quit']
    while True:
        print_actions(action)
        action_choice = int(input(""))
        if action_choice == 3:
            break
        elif action_choice == 2:
            print_items(inventory)
        elif action_choice == 1:
            choose_room()
        else:
            print(f"Invalid choice.")


# def player_choice(number):
#     """turn user input and convert it to lowercase"""
#     action_choice = input(number)
#     return action_choice()


def choose_room():
    """user selects which room to go to"""
    print_rooms(rooms)
    print("Type 'back' to go to main menu.")
    while True:
        print("Which room would you like to explore?")
        room_choice = player_choice("")
        if room_choice == 'back':
            break
        elif room_choice in rooms:
            print(f"You are infront of {room_choice}.")
        else:
            print(f"{room_choice.title()} is not one of the choices.")


def print_actions(action):
    """printing actions in the right format"""
    print("What would you like to do?")
    for action_choice in action:
        print(f"{action.index(action_choice)+1}. {action_choice.upper()}")


def print_rooms(rooms):
    """printing rooms that are in the right format"""
    for room_choice in rooms.keys():
        print(f"{rooms.index(room_choice)+1}. {room_choice.upper()}")


def print_items(inventory):
    """printing inventory in the right format"""
    for items in inventory:
        print(f"{inventory.index(items)+1}. {items.upper()}")


play()
