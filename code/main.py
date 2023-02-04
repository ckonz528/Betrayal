import pygame
from sys import exit
import settings as s
from rooms import RoomDeck
from cards import ObjectDeck


class Game:
    def __init__(self) -> None:

        # initialize pygame and create screen
        pygame.init()
        self.screen = pygame.display.set_mode((s.SCREEN_W, s.SCREEN_H))
        pygame.display.set_caption(s.TITLE)

        self.bg = pygame.image.load(s.BG_IMAGE).convert()

        # create decks
        self.room_deck = RoomDeck()
        self.omen_deck = ObjectDeck(s.OMEN_JSON)
        self.item_deck = ObjectDeck(s.ITEM_JSON)

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            self.screen.blit(self.bg, (0, 0))

            pygame.display.update()


if __name__ == '__main__':
    game = Game()
    game.run()
