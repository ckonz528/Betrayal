import pygame
from pygame.sprite import Sprite
import settings as s

'''
Class to construct each individual room tile
input will be a piece of a json file with the room info in it
'''


class Room():
    def __init__(self, tile_info) -> None:
        self.name = tile_info['name']
        self.doors = [d in tile_info['doors'] for d in 'NESW']
        self.card = tile_info['card']
        self.floors = tile_info['floors']

        image_name = self.name.lower().replace(' ', '_').replace("'", '')

        self.surf = pygame.image.load(
            f'{s.ROOM_PATH}{image_name}.png').convert()
        self.surf = pygame.transform.scale(
            self.surf, (s.TILE_SIZE, s.TILE_SIZE))


'''
Class to construct the stack of room tiles 
'''


class RoomDeck():
    def __init__(self, room_info) -> None:
        pass

    def shuffle(self):
        pass

    def draw_tile(self):
        pass
