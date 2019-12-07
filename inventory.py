# Seungyeon Moon
# CS30 P.1
# Nov.25/2019
# inventory for the game

# from map import ViewMap
#
# inventory = ['notebook', 'blueprint']
#
#
# def print_items():
#     """printing inventory in the right format"""
#     for items in inventory:
#         print(f"- {items.upper()}")
#
#
# def choose_item():
#     """user selects which item to use"""
#     print_items()
#     print("Type 'back' to go to main menu.")
#     while True:
#         print("Which item would you like to use?")
#         item_choice = player_choice("")
#         if item_choice == 'back':
#             break
#         elif item_choice in inventory:
#             if item_choice == 'blueprint':
#                 blueprint = ViewMap()
#                 blueprint.print_map()
#             else:
#                 print("Type 'back' to go to main menu.")
#
#
# def player_choice(text):
#     """turn user input and convert it to lowercase"""
#     action_choice = input(text)
#     return action_choice.lower()
#

class Obtainable:
    def __init__(self):
        print("self")

    def __str(self):
        return self.name


class BronzeKey(Obtainable):
    def __init__(self):
        self.name = "bronze key"
        self.find = "safe"
        self.use = "back door"

    def print_item(self):
        print(self.name)


object = Obtainable()
object.print_item()

# class GoldenKey(Obtainable):
#     def __init__(self):
#         self.name = "golden key"
#         self.find = "cabinet"
#         self.use = "lilian's room"
#
# class SilverKey(Obtainable):
#     def __init__(self):
#         self.name = "silver key"
#         self.find = "given"
#         self.use = "lilian's room"
#
# class LittleKey(Obtainable):
#     def __init__(self):
#         self.name = "little key"
#         self.find = "bedside table"
#         self.use = "cabinet"
#
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
