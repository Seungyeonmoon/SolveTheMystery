# Seungyeon Moon
# CS30 P.1
# Nov.25/2019
# rooms for the game

import sys
from map import ViewMap

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
            elif room_choice == "dining room":
                dr = DineRoom(room_choice)
                dr.nothing()
            elif room_choice == "lilian's office":
                rm = Rooms(room_choice)
                rm.unlock()
                gk = GoldenKey('golden key')
                gk.use()
            elif room_choice == "kitchen":
                rm = Rooms(room_choice)
                rm.room_wall()
                kn = Kitchen(room_choice)
                kn.choose_wall()
            elif room_choice == "outside":
                rm = Rooms(room_choice)
                rm.unlock()
                bk = BronzeKey('bronze key')
                bk.use()
            elif room_choice == "jay's room":
                rm = Rooms(room_choice)
                rm.room_wall()
                jr = JayRoom(room_choice)
                jr.choose_wall()
            elif room_choice == "megan's room":
                rm = Rooms(room_choice)
                rm.room_wall()
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
        """front wall"""
        self.place = "fireplace"
        print(f"You are infront of the {self.place}.")
        print("Use an item to turn off the fire.")
        rm = Rooms("lilian's office")
        rm.print_items()
        fk = FilledKettle('filled kettle')
        fk.use()

    def right_wall(self):
        """right wall"""
        self.place = "safe"
        print(f"You are infront of the {self.place}.")
        print("Enter in the password.")
        while True:
            print("Type 'back' to go back.")
            password = player_choice("")
            if password == 'back':
                break
            elif password == 'gjkh':
                print("you open the safe and find a bronze key.")
                bk = BronzeKey('bronze key')
                bk.take()
            else:
                print("That is not the password.")

    def choose_wall(self):
        """user selecting the wall"""
        while True:
            print("Choose a wall:")
            print("Type 'back to go back.")
            wall_choice = player_choice("")
            if wall_choice == 'back':
                break
            elif wall_choice in ['left', 'behind']:
                print(f"There is nothing on {wall_choice} wall.")
            elif wall_choice == "front":
                self.front_wall()
                break
            elif wall_choice == "right":
                self.right_wall()
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
        print(f"You are infront of the {self.place}.")
        print("Use an item to open.")
        Lk = LittleKey('little key')
        Lk.use()

    def right_wall(self):
        "right wall with items to collect"
        self.place = "stove"
        print(f"You are infront of the {self.place}")
        print(f"There is a kettle.")
        kt = Kettle('kettle')
        kt.take()

    def choose_wall(self):
        while True:
            print("Choose a wall:")
            print("Type 'back to go back.")
            wall_choice = player_choice("")
            if wall_choice == 'back':
                break
            elif wall_choice == 'left':
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
        bt = Bucket('bucket')
        bt.use()


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
            print("Choose a wall:")
            print("Type 'back to go back.")
            wall_choice = player_choice("")
            if wall_choice == 'back':
                break
            elif wall_choice in ['left', 'front', 'behind']:
                print(f"There is nothing on {wall_choice} wall.")
            elif wall_choice == "right":
                self.right_wall()
                sys.exit()
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
        "You look under it and find a notebook.")
        nb = Notebook('notebook')
        nb.clue()

    def choose_wall(self):
        "user selecting a wall to explore"
        while True:
            print("Choose a wall:")
            print("Type 'back to go back.")
            wall_choice = player_choice("")
            if wall_choice == 'back':
                break
            elif wall_choice in ['left', 'right', 'behind']:
                print(f"There is nothing on {wall_choice} wall.")
            elif wall_choice == "front":
                self.front_wall()
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
            print("Choose a wall:")
            print("Type 'back to go back.")
            wall_choice = player_choice("")
            if wall_choice == 'back':
                break
            elif wall_choice in ['left', 'front', 'behind']:
                print(f"There is nothing on {wall_choice} wall.")
            elif wall_choice == "right":
                self.right_wall()
                break
            else:
                print("That is not one of the options.")


# ----------------- inventory --------------------


inventory = ['blueprint', 'silver key']


def collect(item):
    inventory.append(item)
    print(f'You now have: {inventory}')


def print_items():
    """printing inventory in the right format"""
    for items in inventory:
        print(f"- {items.upper()}")


def choose_item():
    """user selects which item to use"""
    print_items()
    print("Type 'back' to go to main menu.")
    print("You can view map by typing in 'blueprint'")
    while True:
        item_choice = player_choice("")
        if item_choice == 'back':
            break
        elif item_choice in inventory:
            if item_choice == 'blueprint':
                blueprint = ViewMap()
                blueprint.print_map()
                print("Type 'back' to go to main menu.")
            else:
                print("Type 'back' to go to main menu.")
                print("You can view map by typing in 'blueprint'")
        else:
            print("Type 'back' to go to main menu.")


class Obtainable:
    def __init__(self, item):
        self.item = item

    def take(self):
        print(f"You take the {self.item}.")
        collect(self.item)


class SilverKey(Obtainable):
    def __init__(self, item):
        super().__init__(item)
        # self.item = "silver key"
        # self.find = "given"
        # self.use = "lilian's room"

    def take(self):
        print(f"You take the {self.item}.")
        collect(self.item)

    def use(self):
        while True:
            print("Type 'back' to go back.")
            item_choice = player_choice("")
            if item_choice == 'back':
                break
            elif item_choice in inventory:
                if item_choice == "silver key":
                    print("You open the door.")
                    rm = Rooms("lilian's room")
                    rm.room_wall()
                    Lr = LiRoom("lilian's room")
                    Lr.choose_wall()
                else:
                    print("That is the wrong item!")
            else:
                print("You have not found the item yet.")

# k = SilverKey(input(""))
# k.use()


class LittleKey(Obtainable):
    def __init__(self, item):
        super().__init__(item)
        # self.item = "little key"
        # self.find = "bedside table"
        # self.place = "cabinet"

    def take(self):
        # print(f"On the {self.place}, there is a {self.item}.")
        print(f"You take the {self.item}.")
        collect(self.item)

    def use(self):
        print_items()
        while True:
            print("Type 'back' to go back.")
            item_choice = player_choice("")
            if item_choice == 'back':
                break
            elif item_choice in inventory:
                if item_choice == "little key":
                    print("You open the cabinet door.")
                    print("In it, there is a golden key.")
                    gk = GoldenKey('golden key')
                    gk.take()
                    break
                else:
                    print("That is the wrong item!")
            else:
                print("You have not found the item yet.")


class BronzeKey(Obtainable):
    def __init__(self, item):
        super().__init__(item)
        # self.name = "bronze key"
        # self.find = "safe"
        # self.use = "back door"

    def take(self):
        print(f"You take the {self.item}.")
        collect(self.item)

    def use(self):
        while True:
            print("Type 'back' to go back.")
            item_choice = player_choice("")
            if item_choice == 'back':
                break
            elif item_choice in inventory:
                if item_choice == "bronze key":
                    print("You open the door and step outside.")
                    jt = Outside('outside')
                    jt.just_there()
                else:
                    print("That is the wrong item!")
            else:
                print("You have not found the item yet.")


class GoldenKey(Obtainable):
    def __init__(self, item):
        super().__init__(item)
        # self.name = "golden key"
        # self.find = "cabinet"
        # self.use = "lilian's office"

    def take(self):
        print(f"You take the {self.item}.")
        collect(self.item)

    def use(self):
        while True:
            print("Type 'back' to go back.")
            item_choice = player_choice("")
            if item_choice == 'back':
                break
            elif item_choice in inventory:
                if item_choice == "golden key":
                    print("You open the door.")
                    rm = Rooms("lilian's office")
                    rm.room_wall()
                    Lo = LiOffice("lilian's office")
                    Lo.choose_wall()
                else:
                    print("That is the wrong item!")
            else:
                print("You have not found the item yet.")


class Kettle(Obtainable):
    def __init__(self, item):
        super().__init__(item)
        # self.name = "kettle"
        # self.find = "stove"
        # self.use = "fireplace"

    def take(self):
        print(f"You take the {self.item}.")
        collect(self.item)

    def use(self):
        while True:
            print("Type 'back' to go back.")
            item_choice = player_choice("")
            if item_choice == 'back':
                break
            elif item_choice in inventory:
                if item_choice == "kettle":
                    print("There is no water.")
                else:
                    print("That is the wrong item!")
            else:
                print("You have not found the item yet.")


class FilledKettle(Obtainable):
    def __init__(self, item):
        super().__init__(item)

    def take(self):
        print("You fill the kettle with water.")
        inventory.remove('kettle')
        collect('filled kettle')

    def use(self):
        print("Type 'back' to go back.")
        while True:
            item_choice = player_choice("")
            if item_choice == 'back':
                break
            elif item_choice in inventory:
                if item_choice == "filled kettle":
                    print("You turn off the fire and find a burnt note with "
                    "letters 'gjkh'. It looks like a password of some kind.")
                    break
                else:
                    print("That is the wrong item!")
            else:
                print("You have not found the item yet.")


class Bucket(Obtainable):
    def __init__(self, item):
        super().__init__(item)
        # self.name = "bucket"
        # self.find = "pantry"
        # self.use = "well"

    def take(self):
        print(f"You take the {self.item}.")
        collect(self.item)

    def use(self):
        while True:
            print("Type 'back' to go back.")
            item_choice = player_choice("")
            if item_choice == 'back':
                break
            elif item_choice in inventory:
                if item_choice == "bucket":
                    print("You pull up the water.")
                    print("when pulled up, a bottle with liquid, with inspection, it is diltiazem.")
                    break
                else:
                    print("That is the wrong item!")
            else:
                print("You have not found the item yet.")


class Receipt(Obtainable):
    def __init__(self, item):
        super().__init__(item)
        # self.name = "receipt"
        # self.find = "given"
        # self.use = "clue"

    def take(self):
        print(f"You read the {self.item}.")
        collect(self.item)

    def clue(self):
        if self.item == "receipt":
            print("The receipt reads that Jay bought 'diltiazem' medication 4 days ago.")
            print("Diltiazem: medication for high blood pressure, when "
            "consumed by an individual in large quantities without high blood"
            "pressure, can cause heart failure.")
        else:
            print("That is the wrong item!")

# k = Receipt('receipt')
# k.clue()


class Notebook(Obtainable):
    def __init__(self, item):
        super().__init__(item)
        # self.name = "receipt"
        # self.find = "given"
        # self.use = "clue"

    def take(self):
        print(f"You read the {self.item}.")
        collect(self.item)

    def clue(self):
        if self.item == "notebook":
            print("Megan wrote about family members.")
            print("Lilian: old, but healty, had 3 siblings, parents of Jay, Megan, Abriella, rich")
            print("Jay: in his 30s, has a high blood pressure")
            print("Megan: in her 30s, no health conditions")
            print("Abriella: Youngest of the cousins, in her 20s, has Asthma")
        else:
            print("That is the wrong item!")
