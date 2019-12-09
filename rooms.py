# Seungyeon Moon
# CS30 P.1
# Nov.25/2019
# rooms for the game

from inventory import SilverKey

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

wall = {"l": "left wall",
        "r": "right wall",
        "f": "front wall",
        "b": "back wall"}


def print_rooms():
    """printing rooms that are in the right format"""
    for room_choice in rooms.keys():
        print(f"- {room_choice.upper()}")


def choose_room():
    """user selects which room to go to"""
    print_rooms()
    print("Type 'back' to go to main menu.")
    print("Which room would you like to explore?")
    while True:
        room_choice = player_choice("")
        if room_choice == 'back':
            break
        elif room_choice in rooms:
            print(f"You are infront of {room_choice}.")
            if room_choice == 'kitchen':
                location = Location()
                location.room_wall()
                wall_choice = player_choice("")
                if wall_choice == 'l':
                    room = Kitchen()
                    room.left_wall()
                elif wall_choice == 'r':
                    room = Kitchen()
                    room.right_wall()
                elif wall_choice == 'f':
                    room = Kitchen()
                    room.front_wall()
                elif wall_choice == 'b':
                    room = Kitchen()
                    room.back_wall()
                else:
                    print("That is not one of the choices.")
            else:
                print(f"{room_choice.title()} is not one of the choices.")


def player_choice(text):
    """turn user input and convert it to lowercase"""
    action_choice = input(text)
    return action_choice.lower()


class Location:
    """returns room locations"""
    def __init__(self):
        print("self")

    def room_wall():
        for key, walls in wall.items():
            print(f"- {key}: {walls}")


class DineRoom(Location):
    """starting position of the player"""
    def __init__(self):
        self.room = "Dining Room"
        # key = SliverKey()
        # self.find = key.print_i_name()

    def print_r_name(self):
        return self.room


class Kitchen(Location):
    """outside with items to obtain"""
    def __init__(self):
        self.room = "Kitchen"

    def left_wall(self):
        self.place = "pantry"
        print(f"You are infront of {self.place}.")

    def right_wall(self):
        self.place = "sink"
        print(f"You are infront of {self.place}.")

    def front_wall(self):
        self.place = "cabinet"
        print(f"You are infront of {self.place}.")

    def back_wall(self):
        self.place = "stove"
        print(f"You are infront of {self.place}.")



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


class Hall(Location):
    """nothing to obtain, empty room"""
    def __init__(self):
        self.room = "Hallway"


class LiOffice(Location):
    """outside with items to obtain"""
    def __init__(self):
        self.room = "Lilian's office"
