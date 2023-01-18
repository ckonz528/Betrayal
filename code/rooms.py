import pygame
from pygame.sprite import Sprite
import settings as s
import json
from random import shuffle


class Room():
    def __init__(self, tile_info) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode((s.SCREEN_W, s.SCREEN_H))
        self.name = tile_info['name']
        self.doors = [d in tile_info['doors'] for d in 'NESW']
        self.card = tile_info['card']
        self.floors = tile_info['floors']

        image_name = self.name.lower().replace(' ', '_').replace("'", '')

        self.img = pygame.image.load(
            f'{s.ROOM_PATH}{image_name}.png').convert()
        self.img = pygame.transform.scale(
            self.img, (s.TILE_SIZE, s.TILE_SIZE))


class RoomDeck():
    def __init__(self, room_list) -> None:
        # construct deck of tiles
        self.room_dict = {room_info['name']: Room(
            room_info) for room_info in room_list}

        self.deck = list(self.room_dict.keys())

        # shuffle deck after importing and creating tiles
        self.shuffle()

    def shuffle(self):
        return shuffle(self.deck)

    def draw_tile(self):
        pass


if __name__ == '__main__':
    room_list = json.load(open('../data/rooms.json'))  # list of dictionaries
    room_deck = RoomDeck(room_list)
