import pygame
import settings as s
from rooms import RoomDeck


class Gameboard:
    def __init__(self):

        # get the display surface
        self.display_surf = pygame.display.get_surface()

        self.setup()

    def setup(self):
        # Room tiles
        self.room_deck = RoomDeck()
        self.place_tile()  # test

        # Cards

        # Players

    def place_tile(self):
        # TODO: dynamically choose the floor
        tile = self.room_deck.choose_tile("basement")
        print(tile.name)

        # place tile on screen

    def run(self, dt):

        # drawing logic
        self.display_surf.fill('pink')
