import pygame
import settings as s


class Room(pygame.sprite.Sprite):
    def __init__(self, tile_info: dict) -> None:
        super().__init__()

        self.name = tile_info['name']
        self.doors = tile_info['doors']
        self.card = tile_info['card']
        self.floors = tile_info['floors']
        self.instructions = tile_info['instructions']

        # get or construct image
        image_name = self.name.lower().replace(' ', '_').replace("'", '')

        try:
            self.image = pygame.image.load(
                f'../graphics/rooms/{image_name}.png').convert_alpha()
        except:
            # print(f"Temp image used for {self.name}") # test
            self.image = pygame.Surface((s.TILE_SIZE, s.TILE_SIZE))
            self.image.fill('pink4')

        self.image = pygame.transform.scale(
            self.image, (s.TILE_SIZE, s.TILE_SIZE))

        self.set_pos((0, 0))

    def set_pos(self, new_pos: tuple):
        self.pos = new_pos
        self.rect = self.image.get_rect(topleft=self.pos)
