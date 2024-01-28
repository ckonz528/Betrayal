import pygame
import settings as s
import textwrap


class Overlay:
    def __init__(self) -> None:
        # general setup
        self.display_surface = pygame.display.get_surface()
        self.font = pygame.font.Font('../font/Semi-Coder-Regular.otf', s.TITLE_FONT_SIZE)

        self.padding = s.SPACE

    def display(self, current_player):
        self.player = current_player

        # stats panel
        inv_surf = pygame.Surface((s.MENU_WIDTH, s.SCREEN_H), pygame.SRCALPHA)
        inv_rect = pygame.Rect((0, 0), (s.MENU_WIDTH, s.SCREEN_H))
        pygame.draw.rect(inv_surf, s.PANEL_BKG, inv_rect)
        self.display_surface.blit(inv_surf, inv_rect)

        # current player
        char_surf = self.player.image
        char_rect = char_surf.get_rect(topleft=s.OVERLAY_POSITIONS['char'])
        self.display_surface.blit(char_surf, char_rect)

        # current player name
        name_list = textwrap.wrap(self.player.name, 12)
        name_surfs = self.list_setup(name_list)
        left, top = s.OVERLAY_POSITIONS['name']
        self.show_entries(name_surfs, left, top, s.MENU_WIDTH - left)

        # current player traits
        trait_names = self.player.traits.keys()
        trait_surfs = self.list_setup(trait_names)
        trait_values = self.player.traits.values()
        value_surfs = self.list_setup(trait_values)
        left, top = s.OVERLAY_POSITIONS['traits'] #TODO: change naming to traits
        self.show_entries(trait_surfs, left, top, s.MENU_WIDTH, value_surfs)
        

    def list_setup(self, entry_list):
        text_surfs = []
        element_height = 0

        for item in entry_list:
            text_surf = self.font.render(str(item), False, 'white')
            text_surfs.append(text_surf)
            element_height += text_surf.get_height()

        return text_surfs
    
    def show_entries(self, text_surfs: list, left: int, top: int, width: int, value_surfs: list = None):
        for text_index, text_surf in enumerate(text_surfs):
            # background
            bg_rect = pygame.Rect(left, top, width, text_surf.get_height())
            pygame.draw.rect(self.display_surface, s.PANEL_BKG, bg_rect)

            # display text
            text_rect = text_surf.get_rect(midleft=(bg_rect.left + self.padding, bg_rect.centery))
            self.display_surface.blit(text_surf, text_rect)

            # display value
            if value_surfs != None:
                value_surf = value_surfs[text_index]
                value_rect = value_surf.get_rect(midright=(bg_rect.right - self.padding, bg_rect.centery))
                self.display_surface.blit(value_surf, value_rect)

            top += text_surf.get_height()