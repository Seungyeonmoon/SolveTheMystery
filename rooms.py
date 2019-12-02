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

class Location:
    """returns room locations"""
    def __init__(self):
        self.room


class DineRoom(Location):
    """starting position of the player"""
    def __init__(self):
        self.room = "Dining Room"


class Outside(Location):
    """outside with items to obtain"""
    def __init__(self):
        self.room = "Outside"


class MegRoom(Location):
    """outside with items to obtain"""
    def __init__(self):
        self.room = "Megan's room"


class JayRoom(Location):
    """outside with items to obtain"""
    def __init__(self):
        self.room = "Jay's room"


class AbRoom(Location):
    """outside with items to obtain"""
    def __init__(self):
        self.room = "Abriella's room"


class LiRoom(Location):
    """outside with items to obtain"""
    def __init__(self):
        self.room = "Lilian's room"

class Kitchen(Location):
    """outside with items to obtain"""
    def __init__(self):
        self.room = "Kitchen"


class Hall(Location):
    """nothing to obtain, empty room"""
    def __init__(self):
        self.room = "Hallway"


class LiOffice(Location):
    """outside with items to obtain"""
    def __init__(self):
        self.room = "Lilian's office"


# class EmpRoom(Location):
#     """blank part of masion"""
