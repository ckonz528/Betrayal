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
        self.all_sprites = pygame.sprite.Group()

        self.setup()

    def setup(self):
        # Build decks
        self.room_deck = RoomDeck('../data/rooms.json', 'room')

        # place starting room tiles
        self.place_tile(self.room_deck.get_obj_by_name(
            'Ground Floor Staircase'), (0, 0))
        self.place_tile(self.room_deck.get_obj_by_name(
            'Hallway'), (s.TILE_SIZE, 0))
        self.place_tile(self.room_deck.get_obj_by_name(
            'Entrance Hall'), (2 * s.TILE_SIZE, 0))

        # TODO: dynamically choose the floor
        tile = self.room_deck.choose_card(floor="basement")  # test

        self.omen_deck = Deck('../data/omens.json', 'object')
        self.item_deck = Deck('../data/items.json', 'object')
        self.event_deck = Deck('../data/events.json', 'event')
        self.char_list = Deck('../data/characters.json', 'explorer')

        # Players
        # TODO: make list of players and cycle through them
        player = self.char_list.name_list['Persephone Puleri']

    def place_tile(self, tile: Room, pos: tuple):
        tile.set_pos(pos)
        self.all_sprites.add(tile)
        print(tile.name)  # test

    def run(self, dt):
        # drawing logic
        self.display_surf.fill(s.BG_COLOR)  # background
        self.all_sprites.draw(self.display_surf)
        # self.all_sprites.update(dt)
