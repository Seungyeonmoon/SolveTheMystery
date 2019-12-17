# Seungyeon Moon
# CS30 P.1
# Nov.25/2019
# inventory for the game

from map import ViewMap

inventory = ['notebook', 'blueprint', 'silver key']


def collect(item):
    inventory.append(item)
    print(inventory)


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


def player_choice(text):
    """turn user input and convert it to lowercase"""
    try:
        action_choice = input(text)
        return action_choice.lower()
    except NameError:
        print("Invalid input. Please try again. ")


class Key:
    def __init__(self, item):
        self.item = item

    def take(self):
        print(f"You take the {self.item}.")
        collect(self.item)


class SilverKey(Key):
    def __init__(self, item):
        super().__init__(item)
        # self.item = "silver key"
        # self.find = "given"
        # self.use = "lilian's room"

    def take(self):
        print(f"You take the {self.item}.")
        collect(self.item)

    def use(self):
        if self.item == "silver key":
            print("You open the door and enter the room.")
        else:
            print("That is the wrong item!")

# k = SilverKey(input(""))
# k.use()

class LittleKey(Key):
    def __init__(self):
        super().__init__(item)
        # self.item = "little key"
        # self.find = "bedside table"
        # self.use = "cabinet"

    def take(self):
        print(f"You take the {self.item}.")
        collect(self.item)

    def use(self):
        if self.item == "little key":
            print("You open the cabinet door.")
        else:
            print("That is the wrong item!")


class BronzeKey(Key):
    def __init__(self):
        super().__init__(item)
        # self.name = "bronze key"
        # self.find = "safe"
        # self.use = "back door"

    def take(self):
        print(f"You take the {self.item}.")
        collect(self.item)

    def use(self):
        if self.item == "bronze key":
            print("You open the door and step outside.")
        else:
            print("That is the wrong item!")



class GoldenKey(Obtainable):
    def __init__(self):
        super().__init__(item)
        # self.name = "golden key"
        # self.find = "cabinet"
        # self.use = "lilian's room"

    def take(self):
        print(f"You take the {self.item}.")
        collect(self.item)

    def use(self):
        if self.item == "golden key":
            print("You open the cabinet door.")
        else:
            print("That is the wrong item!")


# class Clue:
#     def __init__(self):
#         print("self")
#
#     def __str__(self):
#         return self.name


# class Kettle(Obtainable):
#     def __init__(self):
#         self.name = "kettle"
#         self.find = "stove"
#         self.use = "fireplace"
#
# class Bucket(Obtainable):
#     def __init__(self):
#         self.name = "bucket"
#         self.find = "pantry"
#         self.use = "well"
#
# class Bottle(Obtainable):
#     def __init__(self):
#         self.name = "bottle"
#         self.find = "well"
#         self.use = "clue"
#
# class Receipt(Obtainable):
#     def __init__(self):
#         self.name = "receipt"
#         self.find = "given"
#         self.use = "clue"
