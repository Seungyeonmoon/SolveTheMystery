# Seungyeon Moon
# CS30 P.1
# Nov.15/2019
# Menu for the game

import map
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
            map.choose_item()
        elif action_choice == 'explore rooms':
            choose_room()
        else:
            print(f"{action_choice} is not one of the choices.")


def player_choice(text):
    """turn user input and convert it to lowercase"""
    action_choice = input(text)
    return action_choice.lower()


def choose_room():
    """user selects which room to go to"""
    rooms.print_rooms()
    print("Type 'back' to go to main menu.")
    while True:
        print("Which room would you like to explore?")
        room_choice = player_choice("")
        if room_choice == 'back':
            break
        elif room_choice in rooms:
            print(f"You are infront of {room_choice}.")
        else:
            print(f"{room_choice.title()} is not one of the choices.")


def print_actions(action):
    """printing actions in the right format"""
    print("What would you like to do?")
    for action_choice in action:
        print(f"- {action_choice.upper()}")


play()
