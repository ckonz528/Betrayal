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
        self.rotate_timer = Timer(500)
        self.set_pos((0, 0))
        
        self.last_placed_tile = False

    def set_pos(self, grid_pos: tuple):
        self.grid_pos = grid_pos
        self.pos = (self.grid_pos[0] * s.TILE_SIZE, self.grid_pos[1] * s.TILE_SIZE)
        self.rect = self.image.get_rect(topleft=self.pos)

        if self.name not in s.INNATE_ROOMS:
            self.last_placed_tile = True

    def rotate(self):
        keys = pygame.key.get_pressed()

        if not self.rotate_timer.active:
            if keys[pygame.K_RIGHTBRACKET]: # rotate right
                self.doors = self.doors[-1:] + self.doors[:-1]
                print(f'{self.name} doors: {self.doors}')
                self.image = pygame.transform.rotate(self.image, 90)
                self.rotate_timer.activate()
            elif keys[pygame.K_LEFTBRACKET]: # rotate left
                self.doors = self.doors[1:] + self.doors[:1]
                print(f'{self.name} doors: {self.doors}')
                self.image = pygame.transform.rotate(self.image, -90)
                self.rotate_timer.activate()
            elif keys[pygame.K_RETURN]: # confirm position
                # TODO: add visual indicator that a tile can still rotate
                # TODO: confirm that tile rotation is valid
                print(f'stop rotation for {self.name}')
                self.last_placed_tile = False

            self.rect = self.image.get_rect(topleft=self.pos)

    def update(self, dt):
        if self.last_placed_tile:
            self.rotate()
        self.rotate_timer.update()