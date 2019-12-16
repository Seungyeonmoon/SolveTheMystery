# Seungyeon Moon
# CS30 P.1
# Nov.25/2019
# inventory for the game

from map import ViewMap

inventory = ['notebook', 'blueprint', 'silver key']

def collect(item):
    inventory.append(item)


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


class Obtainable:
    def __init__(self):
        print("self")

    def __str__(self):
        return self.name


class SilverKey(Obtainable):
    def __init__(self):
        self.name = "silver key"
        self.find = "given"
        self.use = "lilian's room"

    def print_i_name(self):
        print(self.name)


class LittleKey(Obtainable):
    def __init__(self):
        self.name = "little key"
        self.find = "bedside table"
        self.use = "cabinet"


# class BronzeKey(Obtainable):
#     def __init__(self):
#         self.name = "bronze key"
#         self.find = "safe"
#         self.use = "back door"
#
#     def print_i_name(self):
#         print(self.name)

# class GoldenKey(Obtainable):
#     def __init__(self):
#         self.name = "golden key"
#         self.find = "cabinet"
#         self.use = "kitchen"

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
