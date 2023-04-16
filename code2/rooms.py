import pygame
import settings as s


class Room():
    def __init__(self, tile_info: dict) -> None:
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
