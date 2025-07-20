def armory(item_deck: object):
    # When you discover this tile, reveal cards from the top of the Item deck until you reveal a weapon. Take it and bury the rest.
    pass

def chapel(player):
    # When you discover this tile, gain 1 Sanity
    player.adjust_stat("sanity", 1)

def collapsed_room(player):
    # If you end your turn on this tile, make a Speed roll. 5+ Nothing happens. 4-0 Place your explorer on the Basement Landing and take one die of Physical damage
    roll_result = 2 # speed roll

    if roll_result >= 5:
        pass
    else:
        print("Place your explorer in the Basement Landing.")

        physical_damage = 1 #TODO roll for 1 die of damage amount
        for _ in range(physical_damage):
            chosen_stat = "might" #TODO get player input for which physical trait
            player.adjust_stat(chosen_stat, 1)

def furnace_room(player):
    # If you end your turn on this tile, take 1 Physical damage
    physical_damage = 1 #TODO roll for 1 die of damage amount
    for _ in range(physical_damage):
        chosen_stat = "might" #TODO get player input for which physical trait
        player.adjust_stat(chosen_stat, -1)

def gymnasium(player):
    # When you discover this tile, gain 1 speed
    player.adjust_stat("speed", 1)

def junk_room():
    # When you discover this tile, place an Obstacle token on it
    pass

def larder(player):
    # When you discover this tile, gain 1 Might
    player.adjust_stat("might", 1)

def library(player):
    # When you discover this tile, gain 1 Knowledge
    player.adjust_stat("knowledge", 1)

def panic_room():
    # When you discover this tile, if the Secret Stairs tile has not been placed, find it in the tile stack and place it in the Basement. then, shuffle the tile stack
    pass

def vault(player):
    # Draw 2 items
    pass