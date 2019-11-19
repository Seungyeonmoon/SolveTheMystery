# Seungyeon Moon
# CS30 P.1
# Nov.18/2019
# Map for the game

import inventory
import main

# def map():
#     """Print a blueprint of the mansion"""
#     print_map = """
#     Outside | Kitchen     | Megan's room    | Jay's room    |
#             | dining room |              Hallway            | Lilian's Office
#                           | Abriella's room | Lilian's room |
#     """
#     print(print_map)

blueprint = [
            ["Outside", "Kitchen", "Megan's room", "Jay's room", " "],
            [" ", "Dining room" , "Hallway", "Hallway", "Lilian's office"],
            [" ", " ", "Abriella's room", "Lilian's rooms", " "]
            ]

def print_map():
    for row in blueprint:
        print(row)


def choose_item():
    """user selects which item to use"""
    inventory.print_items()
    print("Type 'back' to go to main menu.")
    while True:
        print("Which item would you like to use?")
        item_choice = main.player_choice("")
        if item_choice == 'back':
            break
        elif item_choice in inventory:
            if item_choice == 'blueprint':
                print_map()
            else:
                print("Type 'back' to go to main menu.")
