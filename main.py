# Seungyeon Moon
# CS30 P.1
# Nov.15/2019
# Menu for the game

import inventory
import rooms


def play():
    """looping through the game"""
    # directions & actions
    action = ['explore rooms', 'check inventory', 'quit']
    while True:
        print_actions(action)
        action_choice = player_choice("")
        if action_choice == 'quit':
            break
        elif action_choice == 'check inventory':
            inventory.choose_item()
        elif action_choice == 'explore rooms':
            rooms.choose_room()
        else:
            print(f"{action_choice} is not one of the choices.")


def player_choice(text):
    """turn user input and convert it to lowercase"""
    action_choice = input(text)
    return action_choice.lower()


def print_actions(action):
    """printing actions in the right format"""
    print("What would you like to do?")
    for action_choice in action:
        print(f"- {action_choice.upper()}")


play()
