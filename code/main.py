import pygame
from sys import exit
import settings as s


class Game:
    def __init__(self) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode((s.SCREEN_W, s.SCREEN_H))
        pygame.display.set_caption(s.TITLE)
        self.clock = pygame.time.Clock()

        self.bg = pygame.image.load(s.BG_IMAGE).convert()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            dt = self.clock.tick() / 1000  # delta time

            self.screen.blit(self.bg, (0, 0))

            pygame.display.update()


if __name__ == '__main__':
    game = Game()
    game.run()
