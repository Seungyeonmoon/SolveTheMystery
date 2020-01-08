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
    while True:
        print("Which room would you like to explore?")
        room_choice = player_choice("")
        if room_choice == 'back':
            break
        elif room_choice in rooms:
            # print(f"You are at {room_choice}.")
            if room_choice == 'back':
                break
            elif room_choice == "lilian's room":
                rm = Rooms(room_choice)
                rm.unlock()
                sk = SilverKey('silver key')
                sk.use()
                rm.room_wall()
                Lr = LiRoom(room_choice)
                Lr.choose_wall()
            elif room_choice == "dining room":
                dr = DineRoom(room_choice)
                dr.nothing()
            elif room_choice == "lilian's office":
                rm = Rooms(room_choice)
                rm.unlock()
                gk = GoldenKey('golden key')
                gk.use()
                rm.room_wall()
                Lo = LiOffice(room_choice)
                Lo.choose_wall()
            elif room_choice == "kitchen":
                rm = Rooms(room_choice)
                rm.room_wall()
                kn = Kitchen(room_choice)
                kn.choose_wall()
            elif room_choice == "outside":
                os = Rooms(room_choice)
                os.unlock()
                bk = BronzeKey('bronze key')
                bk.use()
                jt = Outside(room_choice)
                jt.just_there()
            elif room_choice == "jay's room":
                rm = Rooms(room_choice)
                rm.room_wall()
                jr = JayRoom(room_choice)
                jr.choose_wall()
            elif room_choice == "megan's room":
                mg = MegRoom(room_choice)
                mg.choose_wall()
            elif room_choice == "abriella's room":
                ab = AbRooom(room_choice)
                ab.nothing()
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


class Rooms:
    "parent class for rooms"
    def __init__(self, room):
        self.room = room

    def unlock(self):
        print("You need to unlock the door to go in.")
        print("Use an item?")
        print_items()

    def print_items(self):
        """printing inventory in the right format"""
        for items in inventory:
            print(f"- {items.upper()}")

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
        "front wall"
        self.place = "fireplace"
        print(f"You are infront of the {self.place}.")
        print("Use an item to turn off the fire.")

    def choose_wall(self):
        "user selecting the wall"
        while True:
            wall_choice = player_choice("")
            if wall_choice in ['left', 'right', 'behind']:
                print(f"There is nothing on {wall_choice} wall.")
            elif wall_choice == "front":
                self.front_wall()
                break
            else:
                print("That is not one of the options.")


class DineRoom(Rooms):
    """dining room with items to obtain"""
    def __init__(self, room):
        super().__init__(room)

    def nothing(self):
        "there is nothing in this room"
        print("There is nothing to be found in the dining room.")
        sys.exit()


class Kitchen(Rooms):
    """kitchen with items to obtain"""
    def __init__(self, room):
        super().__init__(room)

    def front_wall(self):
        "front wall with items to collect"
        self.place = "sink"
        print(f"You are infront of the {self.place}.")
        print("You turn on the tab.")
        if 'kettle' in inventory:
            fk = FilledKettle('filled kettle')
            fk.take()
        else:
            print("You have not found the kettle yet.")

    def behind_wall(self):
        "behind wall with items to collect"
        self.place = "pantry"
        print(f"You are infront of the {self.place}")
        print("You open the door and find a bucket on the floor.")
        bt = Bucket('bucket')
        bt.take()

    def left_wall(self):
        "left wall with items to collect"
        self.place = "cabinet"
        print(f"You are infront of the {self.place}")
        print("Use an item to open.")
        super().print_items()

    def right_wall(self):
        "right wall with items to collect"
        self.place = "stove"
        print(f"You are infront of the {self.place}")
        print(f"There is a kettle.")
        kt = Kettle('kettle')
        kt.take()

    def choose_wall(self):
        while True:
            wall_choice = player_choice("")
            if wall_choice == 'left':
                self.left_wall()
            elif wall_choice == "right":
                self.right_wall()
            elif wall_choice == "front":
                self.front_wall()
            elif wall_choice == "behind":
                self.behind_wall()
            else:
                print("That is not one of the options.")


class Outside(Rooms):
    """outside with clues to obtain"""
    def __init__(self, room):
        super().__init__(room)

    def just_there(self):
        "visible directly when stepped outside"
        self.place = "well"
        print("You look down into the well and find something shiny.")
        print("Use an item to pull the water up.")


class JayRoom(Rooms):
    """jay's room with clues to obtain"""
    def __init__(self, room):
        super().__init__(room)

    def right_wall(self):
        "right wall with clues"
        self.place = "coat hanger"
        print("In the coat, you find a receipt.")
        rt = Receipt('receipt')
        rt.clue()

    def choose_wall(self):
        "user selcting wall"
        while True:
            wall_choice = player_choice("")
            if wall_choice in ['left', 'front', 'behind']:
                print(f"There is nothing on {wall_choice} wall.")
            elif wall_choice == "right":
                self.right_wall()
                break
            else:
                print("That is not one of the options.")


class MegRoom(Rooms):
    """megan's room with clues to obtain"""
    def __init__(self, room):
        super().__init__(room)

    def front_wall(self):
        "front wall with items to collect"
        self.place = "bed"
        print("You are infront of the bed."
        "You look under it and find a notebook")
        nb = Notebook('notebook')
        nb.clue()

    def choose_wall(self):
        "user selecting a wall to explore"
        while True:
            wall_choice = player_choice("")
            if wall_choice in ['left', 'right', 'behind']:
                print(f"There is nothing on {wall_choice} wall.")
            elif wall_choice == "front":
                self.right_wall()
                break
            else:
                print("That is not one of the options.")


class AbRooom(Rooms):
    """abriella's room with clues to obtain"""
    def __init__(self, room):
        super().__init__(room)

    def nothing(self):
        print("There is nothing to be found in Abriella's room.")


class LiRoom(Rooms):
    """lilian's with items to obtain"""
    def __init__(self, room):
        super().__init__(room)

    def right_wall(self):
        "right wall with items to obtain"
        self.place = "bedside table"
        print(f"On the {self.place}, there is little key.")
        Lk = LittleKey('little key')
        Lk.take()

    def choose_wall(self):
        "user selcts which wall to explore"
        while True:
            wall_choice = player_choice("")
            if wall_choice in ['left', 'front', 'behind']:
                print(f"There is nothing on {wall_choice} wall.")
            elif wall_choice == "right":
                self.right_wall()
                break
            else:
                print("That is not one of the options.")

choose_room()
