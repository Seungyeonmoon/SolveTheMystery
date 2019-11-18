# Seungyeon Moon
# CS30 P.1
# Nov.18/2019
# inventory for the game

inventory = ['notebook', 'blueprint']

def print_items():
    """printing inventory in the right format"""
    for items in inventory:
        print(f"- {items.upper()}")
