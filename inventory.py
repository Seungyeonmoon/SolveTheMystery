# Seungyeon Moon
# CS30 P.1
# Nov.25/2019
# inventory for the game

import map

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
                map.print_map()
            else:
                print("Type 'back' to go to main menu.")


def player_choice(text):
    """turn user input and convert it to lowercase"""
    action_choice = input(text)
    return action_choice.lower()
