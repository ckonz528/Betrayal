import pygame
import settings as s
from decks import Deck, RoomDeck
from player import Player
from rooms import Room


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
        # TODO: dynamically choose the floor
        tile = self.room_deck.choose_card(floor="basement")  # test
        self.place_tile(tile, (s.TILE_SIZE, s.TILE_SIZE))  # test

        self.omen_deck = Deck('../data/omens.json', 'object')
        self.item_deck = Deck('../data/items.json', 'object')
        self.event_deck = Deck('../data/events.json', 'event')

        # Players
        # currently implemented with same logic as Pydew Valley
        # self.player = Player((0, 0), self.all_sprites)

    def place_tile(self, tile: Room, pos: tuple = (0, 0)):
        tile.set_pos(pos)
        self.all_sprites.add(tile)
        print(tile.name)  # test

    def run(self, dt):
        # drawing logic
        self.display_surf.fill(s.BG_COLOR)  # background
        self.all_sprites.draw(self.display_surf)
        self.all_sprites.update(dt)
