import pygame
import settings as s
import textwrap


class Messenger:
    def __init__(self) -> None:

        # general setup
        # self.player = current_player
        self.display_surface = pygame.display.get_surface()
        self.font = pygame.font.Font('../font/Semi-Coder-Regular.otf', s.MSG_FONT_SIZE)

        # design parameters
        self.width = s.PANEL_WIDTH
        self.space = s.SPACE * 2  # space between entries
        self.padding = s.SPACE

        # entries
        self.entry_list = []
        self.queue_length = 8

    def add_entry(self, entry:str, color:str = 'white'):
        # entry = (entry, color)
        if len(self.entry_list) <self.queue_length:
            self.entry_list.append((entry, color))
        else:
            self.entry_list = self.entry_list[1:]
            self.entry_list.append((entry, color))

    def show_entries(self):
        rev_entry_list = list(reversed(self.entry_list))
        top = s.POSITIONS['msg'][1]

        for item, color in rev_entry_list:
            for line in textwrap.wrap(item,30):
                text_surf = self.font.render(line, False, color)

                # background
                bg_rect = pygame.Rect(s.POSITIONS['msg'][0], top, self.width, text_surf.get_height())
                pygame.draw.rect(self.display_surface, s.PANEL_BKG, bg_rect)

                # text
                text_rect = text_surf.get_rect(midleft=(bg_rect.left + self.padding, bg_rect.centery))
                self.display_surface.blit(text_surf, text_rect)
                top += text_surf.get_height()

            top +=  self.space

    def clear_queue(self):
        self.entry_list = []

    def update(self):
        self.show_entries()
