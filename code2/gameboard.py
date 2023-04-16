import pygame
import settings as s
from decks import Deck, RoomDeck


class Gameboard:
    def __init__(self):

        # get the display surface
        self.display_surf = pygame.display.get_surface()

        self.setup()

    def setup(self):
        # Room tiles
        self.room_deck = RoomDeck('../data/rooms.json', 'room')
        self.place_tile()  # test

        # Cards
        self.omen_deck = Deck('../data/omens.json', 'object')
        print(self.omen_deck.choose_card().name)  # test

        self.item_deck = Deck('../data/items.json', 'object')
        print(self.item_deck.choose_card().name)  # test

        self.event_deck = Deck('../data/events.json', 'event')
        print(self.event_deck.choose_card().name)  # test

        # Players

    def place_tile(self):
        # TODO: dynamically choose the floor
        tile = self.room_deck.choose_card(floor="basement")
        print(tile.name)

        # place tile on screen

    def run(self, dt):

        # drawing logic
        self.display_surf.fill('pink')
