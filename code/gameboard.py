import pygame
import settings as s
from decks import Deck, RoomDeck
from rooms import Room
from explorers import Explorer


class Gameboard:
    def __init__(self):

        # get the display surface
        self.display_surf = pygame.display.get_surface()

        # sprite groups (to draw and update sprites)
        self.all_sprites = CameraGroup()

        self.setup()

    def setup(self):
        # Build room deck
        self.room_deck = RoomDeck('../data/rooms.json', 'room')

        # place starting room tiles
        self.place_tile('Ground Floor Staircase', (0, 0))
        self.place_tile('Hallway', (s.TILE_SIZE, 0))
        self.place_tile('Entrance Hall', (2 * s.TILE_SIZE, 0))

        # TODO: dynamically choose the floor
        tile = self.room_deck.choose_card(floor="ground")  # test

        # build other decks
        self.omen_deck = Deck('../data/omens.json', 'object')
        self.item_deck = Deck('../data/items.json', 'object')
        self.event_deck = Deck('../data/events.json', 'event')
        self.char_list = Deck('../data/characters.json', 'explorer')

        # Players
        # TODO: set up ability for players to select characters
        # TODO: make list of players and cycle through them
        player = self.char_list.obj_dict['Persephone Puleri'] # test
        player.init_player((s.SCREEN_W // 2, s.SCREEN_H // 2), self.all_sprites) # test

        self.place_tile(tile.name,(2 * s.TILE_SIZE,s.TILE_SIZE)) # test

    def place_tile(self, tile_name: str, pos: tuple):
        tile = self.room_deck.get_obj_by_name(tile_name)
        tile.set_pos(pos)
        self.all_sprites.add(tile)
        print(tile.name)  # test

    def run(self, dt):
        # drawing logic
        self.display_surf.fill(s.BG_COLOR)  # background
        self.all_sprites.custom_draw()
        self.all_sprites.update(dt)


class CameraGroup(pygame.sprite.Group):
    def __init__(self) -> None:
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.offset = pygame.math.Vector2()  # offsets the map to move player

        # camera speed
        self.keyboard_speed = 3
    
    def keyboard_ctrl(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.offset.x -= self.keyboard_speed
        if keys[pygame.K_d]:
            self.offset.x += self.keyboard_speed
        if keys[pygame.K_w]:
            self.offset.y -= self.keyboard_speed
        if keys[pygame.K_s]:
            self.offset.y += self.keyboard_speed

    def custom_draw(self):
        self.keyboard_ctrl()

        # cycle through layers dict and draw layers in order
        for layer in s.LAYERS.values():
            for sprite in self.sprites():
                if sprite.layer == layer:
                    offset_rect = sprite.rect.copy()
                    offset_rect.center -= self.offset
                    self.display_surface.blit(sprite.image, offset_rect)