
# Seungyeon Moon
# CS30 P.1
# Nov.15/2019
# menu for the game

rooms = {
        "dining room": 'where the murder happened',
        "kitchen": {'cabinet': 'golden key',
                    'stove': 'cattle',
                    'pantry': 'bucket on the floor',
                    'sink': 'turn on water tap'
                    },
        "back door": {'well': 'poison bottle'},
        "lilian's room": {'bedside table': 'little key'},
        "lilian's office": {'fireplace': 'note', 'safe': 'bronze key'},
        "jay's room": {'coat hanger': 'recipt'},
        "megan's room": {'under the bed': 'notebook'},
        "abriella's room": 'nothing to be found'
        }


inventory = ['notebook']


def play():
    """looping through the game"""
    # directions & actions
    action = ['explore rooms', 'check inventory', 'quit']
    while True:
        print_actions(action)
        action_choice = input("")
        if action_choice == 'quit':
            break
        elif action_choice == 'check inventory':
            print_items(inventory)
        elif action_choice == 'explore rooms':
            choose_room()
        else:
            print(f"{action_choice} is not one of the choices.")


def player_choice(text):
    """turn user input and convert it to lowercase"""
    action_choice = input(text)
    return action_choice.lower()


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
        print(f"- {action_choice.upper()}")


def print_rooms(rooms):
    """printing rooms that are in the right format"""
    for room_choice in rooms.keys():
        print(f"- {room_choice.upper()}")


def print_items(inventory):
    """printing inventory in the right format"""
    for items in inventory:
        print(f"- {items.upper()}")


play()
