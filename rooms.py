# Seungyeon Moon
# CS30 P.1
# Nov.25/2019
# rooms for the game

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


def print_rooms():
    """printing rooms that are in the right format"""
    for room_choice in rooms.keys():
        print(f"- {room_choice.upper()}")


def choose_room():
    """user selects which room to go to"""
    print_rooms()
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


def player_choice(text):
    """turn user input and convert it to lowercase"""
    action_choice = input(text)
    return action_choice.lower()
