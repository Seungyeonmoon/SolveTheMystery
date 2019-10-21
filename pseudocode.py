# Seungyeon Moon
# # CS30 P.1
# Oct.11/2019
# Pseudocode for the game

# Detective _____ (insert player's name) is invited to a dinner at a mansion.
# 3 other people were invited to a masion: Jay, Megan, Abriella

# The host of this dinner was killed while they were having dinner
# Suspects are Jay, Megan, Abriella

# TYPE: insepct ____ (the host)
    # You inspect her body and you find out that she was poisoned
    # With farther inspection, find a silver key in her pocket
        # choice: call the police, or continue inspectoion on your own

# Rooms to explore:
    # Kitchen, host's bedroom, Jay's room, Megan's room, Abriella's room, back door
# TYPE: inspect ____ (room)
# Kitchen: cabinet, stove, or sink, pantry
    # TYPE: inspect _____ (cabinet, stove, pantry, or sink)
        # cabinet, have to open with a little key
            # in it, there is a golden key
        # stove, a cattle
        # sink, but can turn on water tab
        # pantry, a bucket on the floor
# Back door:
    # need little key to open the door
        # outside, a well
            # well has rope
                # pull up?
                # when pulled up, no bucket
                 # need bucket from pantry and when pulled up, a bottle with
                 # liquid, with inspection, it is poison
# Master bedroom (host's bedroom): bedside table
    # Need silver key to go into the room
    # TYPE: use ____ (silver key)
    # TYPE: inspect _____ (bedside table)
        # Bedside table, a little key is found
# Host's office: fireplace, safe
    # Need a golden key to open
    # TYPE: use ____ (golden key)
    # TYPE: inspect ______ (fireplace, safe)
        # fire place, need to turn off fire
            # pour water from sink into kettle & turn off fire
            # In the ashes, there is a note with 4 numbers, 0117
        # A safe that needs 4 numbers to open
            # in it, a bronze key
# Jay's room: a coat hanger,
    # TYPE: inspect ____ (coat hanger)
        # search the coat, find Recipt
            # the recipe reads that he bought "diltiazem" medication
            # 4 days ago.
                # diltiazem: medication for high blood pressure, when consumed
                # by an individual in large quantities without high blood
                # pressure, can cause heart failure
# Megan's room: under the bed
    # TYPE: inspect under the bed
        # A notebook is found
            # Megan wrote about family members.
            # Host: old, but healty, had 3 siblings, parents of Jay, Megan,
                # Abriella, rich
            # Jay: in his 30s, has a high blood pressure
            # Megan: in her 30s
            # Abriella: Youngest of the cousins, in her 20s, Asthma
# Abriella's room
    # nothing to be found

# The murderer is:
# TYPE: _______ (Jay, Megan, Abriella)
    # (the murder is Jay)
    # IF typed Megan or Abriella:
        # She is not the murderer
