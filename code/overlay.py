import pygame
import settings as s


class Overlay:
    def __init__(self) -> None:
        # general setup
        self.display_surface = pygame.display.get_surface()
        # self.player = player

        # imports
        # overlay_path = '../graphics/overlay/'
        # self.tools_surf = {tool: pygame.image.load(
        #     f'{overlay_path}{tool}.png').convert_alpha() for tool in player.tools}

    def display(self,current_player):
        # tools
        # tool_surf = self.tools_surf[self.player.selected_tool]
        # tool_rect = tool_surf.get_rect(midbottom=s.OVERLAY_POSITIONS['tool'])
        # self.display_surface.blit(tool_surf, tool_rect)

        # inventory panel
        inv_surf = pygame.Surface((s.SCREEN_W / 5, s.SCREEN_H), pygame.SRCALPHA)
        inv_rect = pygame.Rect((0, 0), (s.SCREEN_W / 5, s.SCREEN_H))
        pygame.draw.rect(inv_surf, (0,0,0,255*s.TRANSPARENCY), inv_rect)
        self.display_surface.blit(inv_surf, inv_rect)

        # current player
        char_surf = current_player.image
        char_rect = char_surf.get_rect(midbottom=s.OVERLAY_POSITIONS['char'])
        self.display_surface.blit(char_surf, char_rect)