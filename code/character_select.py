import pygame
import settings as s
from decks import Deck

class Selector():
    def __init__(self, char_deck:Deck):
        # general setup
        self.display_surf = pygame.display.get_surface()
        self.font = pygame.font.Font('../font/Semi-Coder-Regular.otf', s.LIST_FONT_SIZE)

        # data setup
        self.char_deck = char_deck
        self.obj_dict = char_deck.obj_dict

    def display(self):
        self.display_surf.fill(s.PANEL_BKG)

    def update(self):
        self.display()