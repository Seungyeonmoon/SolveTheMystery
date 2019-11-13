rooms =[{"dining room": 'where the murder happened'},
        {"kitchen": {'cabinet': 'golden key',
                    'stove': 'cattle',
                    'pantry': 'bucket on the floor',
                    'sink': 'turn on water tap'
                    }
        },
        {"back door": {'well': 'poison bottle'}},
        {"Lilian's room": {'bedside table': 'little key'}},
        {"Lilian's office": {'fireplace': 'note', 'safe': 'bronze key'}},
        {"Jay's room": {'coat hanger': 'recipt'}},
        {"Megan's room": {'under the bed': 'notebook'}},
        {"Abriella's room": 'nothing to be found'}
        ]


def print_rooms(rooms):
    """printing rooms that are in the right format"""
    for room_choice in rooms:
        room =
        if room in room_choice:
            print(f"{rooms.index(room_choice)+1}. {room.upper()}")

print_rooms(rooms)
