import pygame
from pygame.sprite import Sprite


class Player(Sprite):
    def __init__(self, group) -> None:
        super().__init__(group)
