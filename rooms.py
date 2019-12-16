# Seungyeon Moon
# CS30 P.1
# Nov.25/2019
# rooms for the game

import inventory
import sys

# rooms = {
#         "dining room": 'where the murder happened',
#         "kitchen": {'cabinet': 'golden key',
#                     'stove': 'cattle',
#                     'pantry': 'bucket on the floor',
#                     'sink': 'turn on water tap'
#                     },
#         "back door": {'well': 'poison bottle'},
#         "lilian's room": {'bedside table': 'little key'},
#         "lilian's office": {'fireplace': 'note', 'safe': 'bronze key'},
#         "jay's room": {'coat hanger': 'recipt'},
#         "megan's room": {'under the bed': 'notebook'},
#         "abriella's room": 'nothing to be found'
#         }

rooms = ["dining room",
         "kitchen",
         "back door",
         "lilian's room",
         "lilian's office",
         "jay's room",
         "megan's room",
         "abriella's room"
         ]

wall = {"left": "left wall",
        "right": "right wall",
        "front": "front wall",
        "behind": "back wall"}


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
            if room_choice == 'back':
                break
            elif room_choice == "lilian's room":
                key_room()
        else:
            print(f"{room_choice.title()} is not one of the choices.")


def player_choice(text):
    """turn user input and convert it to lowercase"""
    try:
        action_choice = input(text)
        return action_choice.lower()
    except NameError:
        print("Invalid input. Please try again.")


def print_rooms():
    """printing rooms that are in the right format"""
    for room_choice in rooms:
        print(f"- {room_choice.upper()}")


def room_wall():
    """prints out the list of walls"""
    for key, walls in wall.items():
        print(f"- {key}: {walls}")


def key_room():
    """for rooms that require keys to go in"""
    print("Use an item to open the door.")
    inventory.print_items()
    while True:
        items_choice = player_choice("")
        if items_choice == 'back':
            break
        elif items_choice == "silver key":
            print("You open the door and enter the room.")
            room_wall()
            li_room()
        else:
            print("That is the wrong item!")


def li_room():
    """directions in lilian's room"""
    while True:
        wall_choice = player_choice("")
        if wall_choice == 'back':
            break
        elif wall_choice in ['left', 'front', 'behind']:
            print(f"There is nothing on {wall_choice} wall.")
        elif wall_choice == "right":
            w = LiRoom()
            w.right_wall()
        else:
            print("That is not one of the options.")


class LiRoom:
    """lilian's room with items to obtain"""
    def __init__(self):
        self.room = "Lilian's room"


    def right_wall(self):
        self.place = "bedside table"
        self.item = 'little key'
        print(f"You are infront of {self.place}. On it, there is a {self.item}.")
        print("You grab it and put it into the inventory.")
        inventory.collect(self.item)
        print("You have finished collecting all the clues in this room.")
        sys.exit()


# choose_room()

# ------------ for future use ----------
# class DineRoom:
#     """starting position of the player"""
#     def __init__(self):
#         self.room = "Dining Room"
#         # key = SliverKey()
#         # self.find = key.print_i_name()
#

# class Kitchen:
#     """outside with items to obtain"""
#     def __init__(self):
#         self.room = "Kitchen"
#
#     def intro_text(self):
#         return"""
#         You were invited by Lilian to a dinner at a mansion.
#         Three other people were invited, Jay, Megan, and Abriella.
#         While having dinner, Lilian was killed.
#         The suspects are Jay, Megan, and Abriella.
#         You inspect her body and you find out that she was poisoned.
#         With farther inspection, find a silver key in her pocket.
#         """
#
#     def left_wall(self):
#         self.place = "pantry"
#         print(f"You are infront of {self.place}.")
#
#     def right_wall(self):
#         self.place = "sink"
#         print(f"You are infront of {self.place}.")
#
#     def front_wall(self):
#         self.place = "cabinet"
#         print(f"You are infront of {self.place}.")
#         print(f"You have to unlock the ")
#         choose_item()
#
#     def behind_wall(self):
#         self.place = "stove"
#         self.item = "kettle"
#         print(f"You are infront of {self.place}.")
#         print(f"There is a {self.item}, and you grab it.")
#
#
#
# class Outside:
#     """outside with items to obtain"""
#     def __init__(self):
#         self.room = "Outside"
#
#
# class MegRoom:
#     """outside with items to obtain"""
#     def __init__(self):
#         self.room = "Megan's room"
#
#
# class JayRoom:
#     """outside with items to obtain"""
#     def __init__(self):
#         self.room = "Jay's room"
#
#
# class AbRoom:
#     """outside with items to obtain"""
#     def __init__(self):
#         self.room = "Abriella's room"
#
#
# class Hall:
#     """nothing to obtain, empty room"""
#     def __init__(self):
#         self.room = "Hallway"
#
#
# class LiOffice:
#     """outside with items to obtain"""
#     def __init__(self):
#         self.room = "Lilian's office"
