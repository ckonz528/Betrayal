import pygame
import settings as s
import json
from random import shuffle
from cards import Deck


class Room():
    def __init__(self, tile_info) -> None:
        self.name = tile_info['name']
        self.doors = tile_info['doors']
        self.card = tile_info['card']
        self.floors = tile_info['floors']
        self.instructions = tile_info['instructions']

        image_name = self.name.lower().replace(' ', '_').replace("'", '')

        try:
            self.img = pygame.image.load(
                f'../graphics/rooms/{image_name}.png').convert()
        except:
            self.img = pygame.image.load(
                f'../graphics/rooms/generic.png').convert()

        self.img = pygame.transform.scale(
            self.img, (s.TILE_SIZE, s.TILE_SIZE))


class RoomDeck(Deck):
    def __init__(self, info_path: str, object: str) -> None:
        super().__init__(info_path, object)

    def choose_card(self):
        # draw tiles in order of "stack"
        for chosen_tile in self.name_list:
            tile = self.obj_dict[chosen_tile]
            print(tile.name)

            # check if the tile can be placed in the current floor
            if floor in tile.floors:
                self.name_list.remove(chosen_tile)
                return tile

        # TODO: add logic for if there are no more tiles for that floor


if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((s.SCREEN_W, s.SCREEN_H))
    room_deck = Deck('../data/rooms.json', 'room')
    room_tile = room_deck.choose_card(floor='basement')
    print(room_tile.name)
    print(room_tile.instructions)
