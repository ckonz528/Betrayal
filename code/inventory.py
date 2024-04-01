import pygame
import settings as s
from timer import Timer
import textwrap


class Inventory:
    def __init__(self) -> None:

        # general setup
        self.display_surface = pygame.display.get_surface()
        self.font = pygame.font.Font('../font/Semi-Coder-Regular.otf', s.MSG_FONT_SIZE)
        self.title_font = pygame.font.Font('../font/Semi-Coder-Regular.otf', s.TITLE_FONT_SIZE)

        # display parameters
        self.width = s.MENU_WIDTH
        self.space = 10  # space between elements
        self.padding = s.SPACE

        # text setup
        self.inventory_list = []
        self.use_text = self.font.render('use', False, 'white')
    
        # movement
        self.index = 0
        self.timer = Timer(200)

    def setup(self):
        self.create_panel()
        
        # create text surfaces
        self.text_surfs = []
        self.total_height = 0

        for item in self.inventory_list:
            text_surf = self.font.render(item, False, 'white')
            self.text_surfs.append(text_surf)
            self.total_height += text_surf.get_height() + (self.padding * 2)

        # self.total_height += (len(self.text_surfs) - 1) * self.space
        # self.inv_top = self.title_surf.get_height + self.padding*2
        # self.main_rect = pygame.Rect(s.SCREEN_W - self.width, self.inv_top, self.width, self.total_height)

    def create_panel(self):
        self.main_rect = pygame.Rect(s.SCREEN_W - self.width, 0, self.width, s.SCREEN_H)
        pygame.draw.rect(self.display_surface, s.PANEL_BKG, self.main_rect)
        
        # display title
        self.title_surf = self.title_font.render('Inventory', False, 'white')
        self.show_entry(self.title_surf, 0, False)

    def input(self):
        keys = pygame.key.get_pressed()
        self.timer.update()

        # if keys[pygame.K_ESCAPE]:
        #     self.toggle_menu()

        if not self.timer.active:
            if keys[pygame.K_UP]:
                self.index -= 1
                self.timer.activate()

            if keys[pygame.K_DOWN]:
                self.index += 1
                self.timer.activate()

            # if keys[pygame.K_SPACE]:
            #     self.timer.activate()

            #     # get item
            #     current_item = self.inventory_list[self.index]

                # use

        # clamp values
        if self.index < 0:
            self.index = len(self.inventory_list) - 1
        if self.index > len(self.inventory_list) - 1:
            self.index = 0

    def show_entry(self, text_surf, top: int, selected: bool):
        # background
        bg_rect = pygame.Rect(self.main_rect.left, top, self.width, text_surf.get_height() + (self.padding * 2))
        pygame.draw.rect(self.display_surface, s.PANEL_BKG, bg_rect)

        # text
        text_rect = text_surf.get_rect(midleft=(self.main_rect.left + self.padding, bg_rect.centery))
        self.display_surface.blit(text_surf, text_rect)

        # selected
        if 'Inventory empty' not in self.inventory_list:
            if selected:
                pygame.draw.rect(self.display_surface, 'white', bg_rect, width=4)
                pos_rect = self.use_text.get_rect(midright=(bg_rect.right - self.padding, bg_rect.centery))
                self.display_surface.blit(self.use_text, pos_rect)
                self.show_info()

    def show_info(self):
        if 'Inventory empty' not in self.inventory_list:
            item = self.player.inventory[self.inventory_list[self.index]]

            # display item name
            top = self.inv_top + self.total_height + self.space
            for line in textwrap.wrap(item.name,20):
                text_surf = self.title_font.render(line, False, 'yellow')
                text_rect = text_surf.get_rect(topleft=(self.main_rect.left + self.padding, top))
                self.display_surface.blit(text_surf, text_rect)
                top += text_surf.get_height()

            top += self.space

            # display item type
            text_surf = self.font.render(item.type, False, 'white')
            text_rect = text_surf.get_rect(topleft=(self.main_rect.left + self.padding, top))
            self.display_surface.blit(text_surf, text_rect)
            top += text_surf.get_height() + self.space

            # display item description
            for line in textwrap.wrap(item.description,30):
                text_surf = self.font.render(line, False, 'white')
                text_rect = text_surf.get_rect(topleft=(self.main_rect.left + self.padding, top))
                self.display_surface.blit(text_surf, text_rect)
                top += text_surf.get_height()

            top += self.space

            # display action
            for line in textwrap.wrap(item.action,30):
                text_surf = self.font.render(line, False, 'white')
                text_rect = text_surf.get_rect(topleft=(self.main_rect.left + self.padding, top))
                self.display_surface.blit(text_surf, text_rect)
                top += text_surf.get_height()

        # TODO: clean up, consolidate, and simplify code
        # TODO: add check to make sure text doesn't run off bottom of window
        # TODO: add line breaks in descriptions if possible

    def update(self, current_player):
        self.player = current_player
        self.input()

        # create entry list
        # self.inventory_list = list(self.player.item_inventory.keys()) + list(self.player.omen_inventory.keys())
        self.inventory_list = list(self.player.inventory.keys())
        if not self.inventory_list:
            self.inventory_list = ['Inventory empty']

        self.setup()

        # display entries
        self.inv_top = self.main_rect.top + self.title_surf.get_height() + self.padding*2 + self.space
        top = self.inv_top
        for text_index, text_surf in enumerate(self.text_surfs):
            top += text_index * (text_surf.get_height() + (self.padding * 2))
            self.show_entry(text_surf, top, self.index == text_index)
