import pygame
import settings as s
import textwrap


class Overlay:
    def __init__(self) -> None:
        # general setup
        self.display_surface = pygame.display.get_surface()
        self.font = pygame.font.Font('../font/Semi-Coder-Regular.otf', s.TITLE_FONT_SIZE)

    def display(self,current_player):

        # stats panel
        inv_surf = pygame.Surface((s.MENU_WIDTH, s.SCREEN_H), pygame.SRCALPHA)
        inv_rect = pygame.Rect((0, 0), (s.MENU_WIDTH, s.SCREEN_H))
        pygame.draw.rect(inv_surf, s.PANEL_BKG, inv_rect)
        self.display_surface.blit(inv_surf, inv_rect)

        # current player
        char_surf = current_player.image
        char_rect = char_surf.get_rect(topleft=s.OVERLAY_POSITIONS['char'])
        self.display_surface.blit(char_surf, char_rect)

        # current player name
        top = s.OVERLAY_POSITIONS['name'][1]
        for line in textwrap.wrap(current_player.name,12):
            text_surf = self.font.render(line, False, 'white')
            
            # background
            left = s.OVERLAY_POSITIONS['name'][0]
            bg_rect = pygame.Rect(left, top, s.MENU_WIDTH - left, text_surf.get_height())
            pygame.draw.rect(self.display_surface, s.PANEL_BKG, bg_rect)

            # text
            text_rect = text_surf.get_rect(midleft=(bg_rect.left + 10, bg_rect.centery))
            self.display_surface.blit(text_surf, text_rect)
            top += text_surf.get_height()