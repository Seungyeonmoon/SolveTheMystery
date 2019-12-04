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

    def __str__(self):
        return self.name

    def intro_text(self):
        raise NotImplementedError("Create a subclass instead")


class ViewMap:
    """prints a map"""
    def print_map(self):
        """printing the map"""
        self.bp_print = """
        Outside | Kitchen     | Megan's room    | Jay's room    |
                | dining room |              Hallway            | Lilian's Office
                              | Abriella's room | Lilian's room |
        """
        print(self.bp_print)


blueprint = ViewMap()
blueprint.print_map()

# blueprint = [
#     [Kitchen(0, 0)]
# ]
# print(f"{blueprint}")

# class StartTile(MapTile):
#     """starting location"""
#     def intro_text(self):
#         return"""
#         You were invited by Lilian to a dinner at a mansion.
#         Three other people were invited, Jay, Megan, and Abriella.
#         While having dinner, Lilian was killed.
#         The suspects are Jay, Megan, and Abriella.
#         You inspect her body and you find out that she was poisoned.
#         With farther inspection, find a silver key in her pocket.
#         """
#
#
# class BoringTile(MapTile):
#
#     def intro_text(self):
#         return"""
#         Nothing found here
#         """


def tile_at(x, y):
    if x < 0 or y < 0:
        return None
    try:
        return blueprint[y][x]
    except IndexError:
        return None
