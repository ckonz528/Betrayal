import pygame
from sys import exit
import settings as s
from gameboard import Gameboard
from messenger import Messenger


class Game:
    def __init__(self) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode((s.SCREEN_W, s.SCREEN_H))
        pygame.display.set_caption(s.TITLE)
        self.clock = pygame.time.Clock()
        self.messenger = Messenger()
        self.gameboard = Gameboard(self.messenger)

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

                if event.type == pygame.KEYDOWN:
                    keys = pygame.key.get_pressed()
                    if keys[pygame.K_q]:
                        pygame.quit()
                        exit()

            dt = self.clock.tick() / 1000  # delta time
            self.gameboard.run(dt)
            pygame.display.update()


if __name__ == '__main__':
    game = Game()
    game.run()
