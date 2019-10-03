# lists
suspects = ['Jay', 'Megan', 'Abriella']
rooms = ['living room', 'bedroom 1', 'bedroom 2']
found_items = ['notebook']
missing_items = ['golden key', 'silver key', 'cup']


# prints out numerical list of suspects
print(f"Suspects:")
for persons in suspects:
    print(f"{suspects.index(persons)+1}. {persons.title()}")

# prints out numerical list of rooms
print(f"Rooms:")
for area in rooms:
    print(f"{rooms.index(area)+1}. {area.title()}")

# prints out numerical list of found items
print(f"Available items:")
for items in found_items:
    print(f"{found_items.index(items)+1}. {items.title()}")

# prints out numerical list of missing items
print(f"Unavailable items:")
for items in missing_items:
    print(f"{missing_items.index(items)+1}. {items.title()}")
