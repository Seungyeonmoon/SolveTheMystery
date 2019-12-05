# Seungyeon Moon
# CS30 P.1
# Nov.25/2019
# inventory for the game

from map import ViewMap

inventory = ['notebook', 'blueprint']


def print_items():
    """printing inventory in the right format"""
    for items in inventory:
        print(f"- {items.upper()}")


def choose_item():
    """user selects which item to use"""
    print_items()
    print("Type 'back' to go to main menu.")
    while True:
        print("Which item would you like to use?")
        item_choice = player_choice("")
        if item_choice == 'back':
            break
        elif item_choice in inventory:
            if item_choice == 'blueprint':
                blueprint = ViewMap()
                blueprint.print_map()
            else:
                print("Type 'back' to go to main menu.")


def player_choice(text):
    """turn user input and convert it to lowercase"""
    action_choice = input(text)
    return action_choice.lower()


class Obtainable:
    def __init__(self):
        raise NotImplementedError("Do not create raw Obtainable items")


class BronzeKey(Obtainable):
    def __init__(self):
        self.name = "bronze key"

class GoldenKey(Obtainable):
    def __init__(self):
        self.name = "golden key"

class SilverKey(Obtainable):
    def __init__(self):
        self.name = "silver key"

class LittleKey(Obtainable):
    def __init__(self):
        self.name = "little key"

class Cattle(Obtainable):
    def __init__(self):
        self.name = "cattle"

class Bucket(Obtainable):
    def __init__(self):
        self.name = "bucket"

class Bottle(Obtainable):
    def __init__(self):
        self.name = "bottle"

class Receipt(Obtainable):
    def __init__(self):
        self.name = "receipt"
