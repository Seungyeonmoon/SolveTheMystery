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

blueprint = [
            ["Outside", "Kitchen", "Megan's room", "Jay's room", "        "],
            ["       ", "Dining room" , "Hallway", "Hallway", "Lilian's office"],
            ["       ", "        ", "Abriella's room", "Lilian's rooms", " "]
            ]

def print_map():
    for row in blueprint:
        print(row)
