import pygame
import settings as s
import textwrap
from timer import Timer


class Message:
    def __init__(self) -> None:

        # general setup
        # self.player = current_player
        self.display_surface = pygame.display.get_surface()
        self.font = pygame.font.Font('../font/Semi-Coder-Regular.otf', s.MSG_FONT_SIZE)

        # design parameters
        self.width = s.MENU_WIDTH
        self.space = 0  # space between elements
        self.padding = s.SPACE

        # entries
        self.entry_list = []

    def create_text_surfaces(self):
        # create text surfaces
        self.text_surfs = []
        self.total_height = 0

        for item in self.entry_list:
            for line in textwrap.wrap(item,30):
                text_surf = self.font.render(line, False, 'White')
                self.text_surfs.append(text_surf)
                self.total_height += text_surf.get_height()

        self.total_height += (len(self.text_surfs) - 1) * s.SPACE
        self.main_rect = pygame.Rect(s.OVERLAY_POSITIONS['msg'][0], s.OVERLAY_POSITIONS['msg'][1], self.width, self.total_height)

    def add_entry(self, entry:str):
        if len(self.entry_list) <5:
            self.entry_list.append(entry)
        else: 
            self.entry_list = self.entry_list[1:]
            self.entry_list.append(entry)

    def show_entry(self, text_surf, top):
        # background
        bg_rect = pygame.Rect(self.main_rect.left, top, self.width, text_surf.get_height())
        pygame.draw.rect(self.display_surface, s.PANEL_BKG, bg_rect)

        # text
        text_rect = text_surf.get_rect(midleft=(self.main_rect.left + self.padding, bg_rect.centery))
        self.display_surface.blit(text_surf, text_rect)


    def update(self):
        self.create_text_surfaces()

        for text_index, text_surf in enumerate(self.text_surfs):
            top = self.main_rect.top + text_index * (text_surf.get_height() + (self.padding * 2) + self.space)
            self.show_entry(text_surf, top)
