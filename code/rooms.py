import pygame
import settings as s
from timer import Timer
from messenger import Messenger
import room_fxns
import string


class Room(pygame.sprite.Sprite):
    def __init__(self, tile_info: dict, messenger: Messenger) -> None:
        super().__init__()
        self.messenger = messenger

        # basic info
        self.name = tile_info['name']
        self.doors = tile_info['doors']
        self.card = tile_info['card']
        self.floors = tile_info['floors']
        self.instructions = tile_info['instructions']

        # room function
        try:
            fxn_name = self.name.translate(str.maketrans('', '', string.punctuation)).lower().replace(" ","_")
            self.room_fxn = getattr(room_fxns, fxn_name)
        except:
            self.room_fxn = None

        # get or construct image
        image_name = self.name.lower().replace(' ', '_').replace("'", '')

        try:
            self.image = pygame.image.load(f'../graphics/rooms/{image_name}.jpg').convert_alpha()
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

        self.rotateable = False

    def set_pos(self, grid_pos: tuple, direction:str = 'N'):
        self.grid_pos = grid_pos
        self.pos = (self.grid_pos[0] * s.TILE_SIZE, self.grid_pos[1] * s.TILE_SIZE)
        self.rect = self.image.get_rect(topleft=self.pos)

        if self.name not in s.INNATE_ROOMS:
            self.rotateable = True

        self.direction_entered = direction

    def rotate(self):
        keys = pygame.key.get_pressed()

        if not self.rotate_timer.active:
            if keys[pygame.K_RIGHTBRACKET]: # rotate right
                self.doors = self.doors[-1:] + self.doors[:-1]
                self.image = pygame.transform.rotate(self.image, -90)
                self.rotate_timer.activate()
            elif keys[pygame.K_LEFTBRACKET]: # rotate left
                self.doors = self.doors[1:] + self.doors[:1]
                self.image = pygame.transform.rotate(self.image, 90)
                self.rotate_timer.activate()
            elif keys[pygame.K_RETURN]: # confirm position
                # TODO: add visual indicator that a tile can still rotate
                self.rotate_timer.activate()
                if self.rotation_check():
                    self.messenger.add_entry(f'Rotation stopped for {self.name}')
                    self.stop_rotation()

            self.rect = self.image.get_rect(topleft=self.pos)

    def stop_rotation(self):
        self.rotateable = False

    def rotation_check(self):
        #TODO: find a way to run this with the end turn proceedure and keep turn from ending if invalid
        if self.direction_entered == 'N' and self.doors[2]:
            return True
        elif self.direction_entered == 'S' and self.doors[0]:
            return True
        elif self.direction_entered == 'E' and self.doors[3]:
            return True
        elif self.direction_entered == 'W' and self.doors[1]:
            return True

        self.messenger.add_entry(f'Rotation not valid for {self.name}', 'red')
        return False

    def update(self, dt):
        if self.rotateable:
            self.rotate()
        self.rotate_timer.update()
