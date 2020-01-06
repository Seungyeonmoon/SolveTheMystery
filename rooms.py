# Seungyeon Moon
# CS30 P.1
# Nov.25/2019
# rooms for the game

import inventory
from inventory import *
import sys

rooms = ["dining room",
         "kitchen",
         "outside",
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
            print(f"You are at {room_choice}.")
            if room_choice == 'back':
                break
            # elif room_choice == "lilian's room":
            #     key_room()
            elif room_choice == "dining room":
                dr = DineRoom(room_choice)
                dr.nothing()
            # elif room_choice == "lilian's office":
            #     Lo = LiOffice(room_choice)
            #     Lo.front_wall()
            # elif room_choice == "outside":
            #     os = Outside(room_choice)
            #     os.just_there()
            # elif room_choice == "kitchen":
            #
            # elif room_choice == "dining room":
            #     dr = Rooms(room_choice)
            #     rw = DineRoom(room_choice)
            #     rw.nothing()
            # elif room_choice == "outside":
            #     os = Rooms(room_choice)
            #     os.unlock()
            #     jt = Outside(room_choice)
            #     jt.just_there()
            # elif room_choice == "lilian's office":
            #
            # elif room_choice == "jay's room":
            #
            # elif room_choice == "megan's room":
            #
            # elif room_choice == "abriella's room":
            #     print("There is nothing to be found.")
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
        print(f" - {room_choice.upper()}")


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
        print(f"You are infront of {self.place}. On it, there is {self.item}.")
        inventory.collect(self.item)
        print("You have finished collecting all the clues in this room.")
        sys.exit()


class Rooms:
    def __init__(self, room):
        self.room = room

    def print_items(self):
        """printing inventory in the right format"""
        for items in inventory:
            print(f"- {items.upper()}")

    def unlock(self):
        print("You need to unlock the door to go in.")
        print("Use an item?")
        print_items(self)

    def room_wall(self):
        """prints out the list of walls"""
        print(f"You are in {self.room}.")
        print("Which wall would you like to look at?")
        for key, walls in wall.items():
            print(f" - {key}: {walls}")


class LiOffice(Rooms):
    """Lilian's office with items to obtain"""
    def __init__(self, room):
        super().__init__(room)

    def front_wall(self):
        self.place = "fireplace"
        print(f"You are infront of the {self.place}.")
        print("Use an item to turn off the fire.")


class DineRoom(Rooms):
    """dining room with items to obtain"""
    def __init__(self, room):
        super().__init__(room)

    def nothing(self):
        print("There is nothing to be found in the dining room.")
        sys.exit()


class Kitchen(Rooms):
    """kitchen with items to obtain"""
    def __init__(self, room):
        super().__init__(room)

    def front_wall(self):
        self.place = "sink"
        print(f"You are infront of the {self.place}")
        print("turn on the tab")

    def behind_wall(self):
        self.place = "pantry"
        print(f"You are infront of the {self.place}")
        print("You open the door and find a bucket on the floor.")

    def left_wall(self):
        self.place = "cabinet"
        print(f"You are infront of the {self.place}")
        print("Use an item to open.")

    def right_wall(self):
        self.place = "stove"
        print(f"You are infront of the {self.place}")
        print(f"There is a kettle.")


class Outside(Rooms):
    """outside with clues to obtain"""
    def __init__(self, room):
        super().__init__(room)

    def just_there(self):
        self.place = "well"
        print("You look down into the well and find something shiny.")
        print("Use an item to pull the water up.")


class JayRoom(Rooms):
    """jay's room with clues to obtain"""
    def __init__(self, room):
        super().__init__(room)

    def right_wall(self):
        self.place = "coat hanger"
        print("In the coat, you find a receipt")


class MegRoom(Rooms):
    """megan's room with clues to obtain"""
    def __init__(self, room):
        super().__init__(room)

    def front_wall(self):
        self.place = "bed"
        print("You are infront of the bed."
        "You look under it and find a notebook")


class AbRooom(Rooms):
    """abriella's room with clues to obtain"""
    def __init__(self, room):
        super().__init__(room)

    def nothing(self):
        print("There is nothing to be found in Abriella's room.")


# class LiRoom(Rooms):
#     """lilian's with items to obtain"""
#     def __init__(self, room):
#         super().__init__(room)
#
#     def right_wall(self):
#         self.place = "bedside table"
#         print(f"On the {self.place}, there is little key.")


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
# class Outside:
#     """outside with items to obtain"""
#     def __init__(self):
#         self.room = "Outside"
#
#     def
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
