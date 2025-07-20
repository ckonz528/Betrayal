import pygame
import settings as s
import textwrap

class Event:
    def __init__(self) -> None:

        # general setup
        self.display_surface = pygame.display.get_surface()

        # font sizes
        self.font = pygame.font.Font('../font/Semi-Coder-Regular.otf', s.EVENT_TEXT_SIZE)
        self.title_font = pygame.font.Font('../font/Semi-Coder-Regular.otf', s.EVENT_TITLE_SIZE)

        # display parameters
        self.window_width = s.POPUP_WIDTH
        self.window_height = s.POPUP_HEIGHT
        self.window_width_chars = 62
        self.space = 20  # space between elements
        self.padding = s.SPACE

        self.event_state = ["description", "action", "result"]

        # self.input_timer = Timer()

    def run_event(self, event_card):
        self.event = event_card
        print(f'Event function = {self.event.event_fxn}')

    def event_window(self):
        self.event_rect = pygame.Rect((s.POSITIONS['roller']), (self.window_width, self.window_height))
        pygame.draw.rect(self.display_surface, s.EVENT_BKG, self.event_rect, border_radius=12)

        self.show_info()

        text = '[PRESS ENTER TO CONTINUE]'
        text_surf = self.font.render(text, False, 'white')
        text_rect = text_surf.get_rect(midbottom=(self.event_rect.midbottom[0], self.event_rect.midbottom[1]))
        self.display_surface.blit(text_surf, text_rect)

    def show_info(self):
        # display event name
        top = self.event_rect.top + self.space
        for line in textwrap.wrap(self.event.name, 20):
            text_surf = self.title_font.render(line, False, 'white')
            text_rect = text_surf.get_rect(topleft=(self.event_rect.left + self.padding, top))
            self.display_surface.blit(text_surf, text_rect)
            top += text_surf.get_height()

        top += self.space

        # display item description
        for line in textwrap.wrap(self.event.description, self.window_width_chars):
            text_surf = self.font.render(line, False, 'white')
            text_rect = text_surf.get_rect(topleft=(self.event_rect.left + self.padding, top))
            self.display_surface.blit(text_surf, text_rect)
            top += text_surf.get_height()

        top += self.space

        # display action
        for line in textwrap.wrap(self.event.action_text, self.window_width_chars):
            text_surf = self.font.render(line, False, 'white')
            text_rect = text_surf.get_rect(topleft=(self.event_rect.left + self.padding, top))
            self.display_surface.blit(text_surf, text_rect)
            top += text_surf.get_height()

    # def input(self):
    #     keys = pygame.key.get_pressed()

    #     if not self.input_timer.active:
    #         if keys[pygame.K_RETURN]:
    #             pass

    def update(self):
        self.event_window()
        # self.input_timer.update()
        # self.input()
