import pygame
import settings as s
from timer import Timer


class Menu:
    def __init__(self, current_player) -> None:

        # general setup
        self.player = current_player
        self.display_surface = pygame.display.get_surface()
        self.font = pygame.font.Font('../font/Semi-Coder-Regular.otf', 30)

        # trait_list
        self.width = 400
        self.space = 10  # space between elements
        self.padding = 8

        # entries
        self.trait_list = list(self.player.traits.keys())
        self.setup()

        # movement
        self.index = 0
        self.timer = Timer(200)

    def setup(self):
        # create text surfacces
        self.text_surfs = []
        self.total_height = 0

        for item in self.trait_list:
            text_surf = self.font.render(item, False, 'Black')
            self.text_surfs.append(text_surf)
            self.total_height += text_surf.get_height() + (self.padding * 2)

        self.total_height += (len(self.text_surfs) - 1) * self.space
        self.menu_top = s.SCREEN_H / 2 - self.total_height / 2
        self.main_rect = pygame.Rect(
            s.SCREEN_W / 2 - self.width / 2, self.menu_top, self.width, self.total_height)

    def input(self):
        pass

    def show_entry(self, text_surf, value, top):
        # background
        bg_rect = pygame.Rect(self.main_rect.left, top, self.width,
                              text_surf.get_height() + (self.padding * 2))
        pygame.draw.rect(self.display_surface, 'White', bg_rect, 0, 6)

        # text
        text_rect = text_surf.get_rect(midleft=(self.main_rect.left + self.space, bg_rect.centery))
        self.display_surface.blit(text_surf, text_rect)

        # value
        value_surf = self.font.render(str(value), False, 'Black')
        value_rect = value_surf.get_rect(
            midright=(self.main_rect.right - self.space, bg_rect.centery))
        self.display_surface.blit(value_surf, value_rect)


    def update(self, current_player):
        # self.input()
        self.player = current_player

        for text_index, text_surf in enumerate(self.text_surfs):
            top = self.main_rect.top + text_index * \
                (text_surf.get_height() + (self.padding * 2) + self.space)
            value_list = list(self.player.traits.values()) + \
                list(self.player.traits.values())
            value = value_list[text_index]
            self.show_entry(text_surf, value, top)
