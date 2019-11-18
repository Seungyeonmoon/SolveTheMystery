# Seungyeon Moon
# CS30 P.1
# Nov.18/2019
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
