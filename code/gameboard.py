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
        # Grid
        self.grid = {}

        # Room deck
        self.room_deck = RoomDeck('../data/rooms.json', 'room')

        # place starting room tiles
        self.place_tile('Ground Floor Staircase', (-2, 0))
        self.place_tile('Hallway', (-1, 0))
        self.place_tile('Entrance Hall', (0,0))
        self.place_tile('Upper Landing', (100,0))
        self.place_tile('Basement Landing', (-100,0))

        # TODO: dynamically choose the floor
        tile = self.room_deck.choose_card(floor="ground")  # test
        self.place_tile(tile.name,(0,1)) # test

        # Card decks
        self.omen_deck = Deck('../data/omens.json', 'object')
        self.item_deck = Deck('../data/items.json', 'object')
        self.event_deck = Deck('../data/events.json', 'event')
        self.char_list = Deck('../data/characters.json', 'explorer')

        # Players
        # TODO: set up ability for players to select characters
        # TODO: make list of players and cycle through them
        player = self.char_list.obj_dict['Persephone Puleri'] # test
        player.init_player((0,0), self.all_sprites) # test

    def place_tile(self, tile_name: str, grid_pos: tuple):
        tile = self.room_deck.get_obj_by_name(tile_name)
        tile.set_pos(grid_pos)
        self.grid[grid_pos] = tile.name
        self.all_sprites.add(tile)
        print(tile.name)  # test
        print(self.grid)

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

        # TODO: set up to snap camera to player position
        # snap camera to original position
        if keys[pygame.K_g]: # ground floor (Entrance Hall)
            self.set_camera(pygame.math.Vector2((-2 * s.TILE_SIZE, -s.TILE_SIZE)))
        elif keys[pygame.K_u]: # upper landing
            self.set_camera(pygame.math.Vector2((98 * s.TILE_SIZE, -s.TILE_SIZE)))
        elif keys[pygame.K_b]: # basement landing
            self.set_camera(pygame.math.Vector2((-102 * s.TILE_SIZE, -s.TILE_SIZE)))

    def custom_draw(self):
        self.keyboard_ctrl()

        # cycle through layers dict and draw layers in order
        for layer in s.LAYERS.values():
            for sprite in self.sprites():
                if sprite.layer == layer:
                    offset_rect = sprite.rect.copy()
                    offset_rect.center -= self.offset
                    self.display_surface.blit(sprite.image, offset_rect)

    def set_camera(self, set_pos):
        # TODO: set up to snap camera to other positions
        self.offset = set_pos
