import pygame
import pygame.transform
import settings as s

class StartScreen:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()
        self.font = pygame.font.Font('../font/Semi-Coder-Regular.otf', s.TITLE_FONT_SIZE)

        self.bkg_img = pygame.image.load('../graphics/start_screen/start_background.jpg').convert_alpha()
        self.bkg_img = pygame.transform.scale(self.bkg_img, (s.SCREEN_W, s.SCREEN_H))
        self.bkg_img_rect = self.bkg_img.get_rect(topleft=(0,0))

        self.logo = pygame.image.load('../graphics/start_screen/betrayal_logo.png').convert_alpha()
        self.logo_rect = self.logo.get_rect(center=(s.SCREEN_W//2, s.SCREEN_H//2))

    def display(self):
        self.display_surface.blit(self.bkg_img, self.bkg_img_rect)
        self.display_surface.blit(self.logo, self.logo_rect)

        text = '[PRESS SPACE TO EMBARK]'
        text_surf = self.font.render(text, False, 'white')
        text_rect = text_surf.get_rect(midtop=(self.logo_rect.midbottom[0], self.logo_rect.midbottom[1] + s.CHAR_SIZE))
        self.display_surface.blit(text_surf, text_rect)

    def update(self):
        self.display()