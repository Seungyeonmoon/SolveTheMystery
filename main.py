# Seungyeon Moon
# CS30 P.1
# Nov.15/2019
# Menu for the game

import sys
import rooms
from rooms import inventory
from map import Start


def play():
    """looping through the game"""
    # directions & actions
    action = ['explore rooms', 'check inventory', 'state murderer', 'quit']
    s = Start('start')
    s.intro_text()
    print("Once you find the 'bronze key', you can state the murderer.")
    while True:
        print_actions(action)
        action_choice = player_choice("")
        if action_choice == 'quit':
            sys.exit()
        elif action_choice == 'check inventory':
            rooms.choose_item()
        elif action_choice == 'explore rooms':
            rooms.choose_room()
        elif action_choice == 'state murderer':
            while True:
                if 'bronze key' in inventory:
                    choose_murderer()
                elif 'bronze key' not in inventory:
                    print("You need to find more clues!")
                    print("Once you find the 'bronze key', you can state the murderer.")
                    break
        else:
            print(f"{action_choice} is not one of the choices.")


def player_choice(text):
    """turn user input and convert it to lowercase"""
    try:
        action_choice = input(text)
        return action_choice.lower()
    except NameError:
        print("Invalid input. Please try again. ")


def print_actions(action):
    """printing actions in the right format"""
    print("What would you like to do?")
    for action_choice in action:
        print(f"- {action_choice.upper()}")


def choose_murderer():
    """player chooses who the murder is"""
    while True:
        print("State the murderer (Jay, Megan, Abriella):")
        murderer_choice = player_choice("")
        if murderer_choice == 'jay':
            print("You have successfully determined the murderer!")
            sys.exit()
        elif murderer_choice == 'abriella':
            print("Unfortunatly, Abriella is not the murderer.")
            print("Please try again.")
        elif murderer_choice == 'megan':
            print("Unfortunatly, Abriella is not the murderer.")
            print("Please try again.")


play()
