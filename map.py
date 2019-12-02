# Seungyeon Moon
# CS30 P.1
# Nov.25/2019
# Map for the game


# def map():
#     """Print a blueprint of the mansion"""
#     print_map = """
#     Outside | Kitchen     | Megan's room    | Jay's room    |
#             | dining room |              Hallway            | Lilian's Office
#                           | Abriella's room | Lilian's room |
#     """
#     print(print_map)

blueprint1 = [
            ["Outside", "Kitchen", "Megan's room", "Jay's room", "  "],
            ["  ", "Dining room", "Hallway", "Hallway", "Lilian's office"],
            ["  ", "  ", "Abriella's room", "Lilian's rooms", "  "]
            ]


# def print_map():
#     for row in blueprint:
#         print(row)

class MapTile:
    """Map with x and y coordinates"""
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Location:
    """map with x and y coordinates"""
    def __init__(self, x, y):
        self.x = x
        self.y = y


class DineRoom(Location):
    """starting position of the player"""
    def __init__(self):
        self.room = "Dining Room"


class Outside(Location):
    """outside with items to obtain"""
    def __init__(self):
        self.room = "Outside"


class MegRoom(Location):
    """outside with items to obtain"""
    def __init__(self):
        self.room = "Megan's room"


class JayRoom(Location):
    """outside with items to obtain"""
    def __init__(self):
        self.room = "Jay's room"


class AbRoom(Location):
    """outside with items to obtain"""
    def __init__(self):
        self.room = "Abriella's room"


class LiRoom(Location):
    """outside with items to obtain"""
    def __init__(self):
        self.room = "Lilian's room"

class Kitchen(Location):
    """outside with items to obtain"""
    def __init__(self):
        self.room = "Kitchen"


class Hall(Location):
    """nothing to obtain, empty room"""
    def __init__(self):
        self.room = "Hallway"


class LiOffice(Location):
    """outside with items to obtain"""
    def __init__(self):
        self.room = "Lilian's office"


# class EmpRoom(Location):
#     """blank part of masion"""

blueprint = [
    # [Outside(0, 0), Kitchen(0, 1), MegRoom(0, 2), JayRoom(0, 3), Hall(0, 4)]
    # [Hall(1, 0), DineRoom(1, 1), Hall(1, 2), Hall(1, 3), LiOffice(1, 4)]
    # [EmpRoom(2, 0)]
    [Outside, Kitchen, MegRoom, JayRoom]
]



print(blueprint)
