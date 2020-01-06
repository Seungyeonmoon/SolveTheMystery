# Seungyeon Moon
# CS30 P.1
# Nov.25/2019
# inventory for the game

from map import ViewMap

inventory = ['blueprint', 'silver key']


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
        if self.item == "silver key":
            print("You open the door and enter the room.")
        else:
            print("That is the wrong item!")

# k = SilverKey(input(""))
# k.use()


class LittleKey(Obtainable):
    def __init__(self, item):
        super().__init__(item)
        # self.item = "little key"
        # self.find = "bedside table"
        self.place = "cabinet"

    def take(self):
        print(f"On the {self.place}, there is a {self.item}.")
        print(f"You take the {self.item}.")
        collect(self.item)

    def use(self):
        if self.item == "little key":
            print("You open the cabinet door.")
        else:
            print("That is the wrong item!")
# k = LittleKey(input(""))
# k.use()


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
        if self.item == "bronze key":
            print("You open the door and step outside.")
        else:
            print("That is the wrong item!")


class GoldenKey(Obtainable):
    def __init__(self, item):
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
        if self.item == "kettle":
            print("You turn off the fire.")
        else:
            print("That is the wrong item!")


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
        if self.item == "bucket":
            print("You pull up the water.")
        else:
            print("That is the wrong item!")


class Bottle(Obtainable):
    def __init__(self, item):
        super().__init__(item)
        # self.name = "bottle"
        # self.find = "well"
        # self.use = "clue"

    def take(self):
        print(f"You take the {self.item}.")
        collect(self.item)

    def clue(self):
        if self.item == "bottle":
            print("It contains poison.")
        else:
            print("That is the wrong item!")


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
            print("The recipe reads that Jay bought 'diltiazem' medication 4 days ago.")
            print("Diltiazem: medication for high blood pressure, when consumed"
            "by an individual in large quantities without high blood"
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


class FilledKettle(Obtainable):
    def __init__(self, item):
        super().__init__(item)

    def take(self):
         collect('filled kettle')
         inventory.remove('kettle')
