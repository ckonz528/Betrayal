import pygame
import settings as s
from timer import Timer


class Room(pygame.sprite.Sprite):
    def __init__(self, tile_info: dict) -> None:
        super().__init__()

        # basic info
        self.name = tile_info['name']
        self.doors = tile_info['doors']
        self.card = tile_info['card']
        self.floors = tile_info['floors']
        self.instructions = tile_info['instructions']

        # get or construct image
        image_name = self.name.lower().replace(' ', '_').replace("'", '')

        try:
            self.image = pygame.image.load(f'../graphics/rooms/{image_name}.png').convert_alpha()
        except:
            # print(f"Temp image used for {self.name}") # test
            self.image = pygame.Surface((s.TILE_SIZE, s.TILE_SIZE))
            self.image.fill('pink4')

        self.image = pygame.transform.scale(
            self.image, (s.TILE_SIZE, s.TILE_SIZE))
        
        # set up object for game use
        self.layer = s.LAYERS['board']

        self.set_pos((0, 0))
        
        self.last_placed_tile = False

    def set_pos(self, new_pos: tuple):
        self.pos = new_pos
        self.rect = self.image.get_rect(topleft=self.pos)

        if self.name not in s.INNATE_ROOMS:
            self.last_placed_tile = True

    def rotate(self):
        keys = pygame.key.get_pressed()

        key_timer = Timer(500)

        if not key_timer.active:
            if keys[pygame.K_RIGHTBRACKET]:
                self.image = pygame.transform.rotate(self.image, 90)
                key_timer.activate()
            elif keys[pygame.K_LEFTBRACKET]:
                self.image = pygame.transform.rotate(self.image, -90)
                key_timer.activate()
            elif keys[pygame.K_RETURN]:
                print(f'stop rotation for {self.name}')
                self.last_placed_tile = False

            self.rect = self.image.get_rect(topleft=self.pos)
            key_timer.update()

    def update(self, dt):
        if self.last_placed_tile:
            self.rotate()
