import pygame
from roller import Roller

def alien_geometry(player):
    roll_result = 2

    if roll_result >= 4:
        player.adjust_stat(stat="sanity", amnt=1)
    else:
        player.adjust_stat(stat="speed", amnt=-1)

def an_eerie_feeling(player):
    roll_result = 2

    if roll_result == 4:
        pass
    elif roll_result == 3:
        player.adjust_stat("speed", -1)
    elif roll_result == 2:
        player.adjust_stat("sanity", -1)
    elif roll_result == 1:
        player.adjust_stat("knowledge", -1)
    else:
        player.adjust_stat("might", -1)

def bat_out_of_hell(player):
    roll_result = 2

    if roll_result >= 4:
        #TODO make this operational
        print("Place your explorer on an adjacent tile")
    else:
        chosen_stat = "might" #TODO get player input for which physical trait
        player.adjust_stat(chosen_stat, -1)

def behind_you(player):
    roll_result = 2

    if roll_result >= 4:
        player.adjust_stat("sanity", 1)
    else:
        chosen_stat = "might" #TODO get player input for which physical trait
        player.adjust_stat(chosen_stat, -1)

def bite(player):
    roll_result = 2

    if roll_result >= 4:
        pass
    if roll_result == 2 or roll_result == 3:
        chosen_stat = "might" #TODO get player input for which physical trait
        player.adjust_stat(chosen_stat, -1)
    else:
        for _ in range(3):
            chosen_stat = "might" #TODO get player input for which physical trait
            player.adjust_stat(chosen_stat, -1)

def brain_food(player):
    roll_result = 2

    if roll_result >= 5:
        chosen_stat = "might" #TODO get player input for which physical trait
        player.adjust_stat(chosen_stat, 1)
    elif roll_result >= 1 and roll_result <= 4:
        player.adjust_stat("speed", 1)
        player.adjust_stat("sanity", -1)
    else:
        for _ in range(2):
            chosen_stat = "knowledge" #TODO get player input for which general trait
            player.adjust_stat(chosen_stat, 1)

def burning_figure(player):
    roll_result = 2

    if roll_result >= 4:
        player.adjust_stat("sanity", 1)
    elif roll_result == 2 or roll_result == 3:
        print("Place your explorer in the Entrance Hall.")
    else:
        physical_damage = 1 #TODO roll for 1 die of damage amount
        for _ in range(physical_damage):
            chosen_stat = "might" #TODO get player input for which physical trait
            player.adjust_stat(chosen_stat, 1)

        mental_damage = 1 #TODO roll for 1 die of damage amount
        for _ in range(mental_damage):
            chosen_stat = "sanity" #TODO get player input for which mental trait
            player.adjust_stat(chosen_stat, 1)

def cassette_player(player):
    roll_result = 2

    if roll_result >= 4:
        player.adjust_stat("knowledge", 1)
    else:
        chosen_stat = "sanity" #TODO get player input for which mental trait
        player.adjust_stat(chosen_stat, -1)

def clown_room(player):
    roll_result = 2

    if roll_result >= 4:
        pass
    else:
        for _ in range(2):
            chosen_stat = "sanity" #TODO get player input for which mental trait
            player.adjust_stat(chosen_stat, -1)