rooms = {
        'dining room': 'where the murder happened',
        'kitchen': {'cabinet': 'golden key',
                    'stove': 'cattle',
                    'pantry': 'bucket on the floor',
                    'sink': 'turn on water tap'
                    },
        'back door': {'well': 'poison bottle'},
        'Lilian\'s room': {'bedside table': 'little key'},
        'Lilian\'s office': {'fireplace': 'note', 'safe': 'bronze key'},
        'Jay\'s room': {'coat hanger': 'recipt'},
        'Megan\'s room': {'under the bed': 'notebook'},
        'Abriella\'s room': 'nothing to be found'
        }

inventory = ['notebook']

actions = ['check inventory', 'explore rooms', 'quit']
directions = ['forward', 'backward', 'left', 'right']

def play():
    # directions & actions
    action = ['explore rooms', 'check inventory', 'quit']
    directions = ['forward', 'backward', 'left', 'right']
    print_actions(action)
    while True:
        action_choice = player_choice("")
        if action_choice in action:
            print(f"{action_choice.title}")
            if action_choice == 'quit':
                break
            elif action_choice == 'check inventory':
                for objects in inventory:
                    print(f"* {objects.upper()}")
            elif action_choice == 'explore rooms':
                choose_room()
            else:
                print(f"{choice.title()} is not one of the choices.")
        else:
            print(f"{player_choice.title()} is not one of the choices.")

def player_choice(text):
    """turn user input and convert it to lowercase"""
    action_choice = input(text)
    return action_choice.lower()

def choose_room():
    """user selects which room to go to"""
    # print("ROOMS:")
    # for room in rooms:
    print(f"{room.upper()}")
    while True:
        input = player_choice("Which room would you like to explore?")
        room_choice = input
        if room_choice in rooms:
            print(f"You are infront of {room_choice}.")
        else:
            print(f"{room_choice.title()} is not one of the choices.")

def print_actions(action):
    print("What would you like to do?")
    for action_choice in action:
        print(f"* {action_choice.upper()}")

play()
