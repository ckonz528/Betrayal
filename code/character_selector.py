import pygame
import pygame.draw
import pygame.font
import settings as s
from decks import Deck
from timer import Timer
import textwrap

class Selector():
    def __init__(self, char_deck:Deck):
        # general setup
        self.display_surf = pygame.display.get_surface()

        # font sizes
        self.title_font = pygame.font.Font('../font/Semi-Coder-Regular.otf', s.TITLE_FONT_SIZE)
        self.font = pygame.font.Font('../font/Semi-Coder-Regular.otf', s.INFO_FONT_SIZE)
        self.player_font = pygame.font.Font('../font/Semi-Coder-Regular.otf', s.EVENT_TITLE_SIZE)

        self.window_width_chars = 78

        # setup
        self.char_deck = char_deck

        self.timer = Timer()

        self.portrait_dict = {}
        self.portrait_setup()

        # status
        self.index = 0
        self.active = False
        self.player_counter = 0
        self.selected_chars = []

        # window properties
        self.window_width = s.POPUP_WIDTH
        self.window_height = s.POPUP_HEIGHT

        self.bg_color = s.DKGRAY
        self.panel_color = s.DKGRAY

        self.bottom_msg = '[Press Enter to select this character]'

    def portrait_setup(self):
        for i, character in enumerate(self.char_deck.obj_dict.values()):
            if i % 2 == 0:
                portrait_x = 0 + 2 * s.MARGIN
            else:
                portrait_x = s.PORTRAIT_SIZE[0] + 4 * s.MARGIN # portrait_x + s.PORTRAIT_SIZE[0] + 2 * s.MARGIN
            portrait_y = s.MARGIN + i // 2 * s.PORTRAIT_SIZE[1]

            self.portrait_dict[character.name] = Portrait(character.name, portrait_x, portrait_y)

        self.portrait_list = list(self.portrait_dict.keys())

    def display(self):
        self.display_surf.fill(self.bg_color)

        # display portraits
        for i, portrait in enumerate(self.portrait_dict.values()):
            self.char_display(portrait, self.index == i)

        # display text window & text
        self.info_window()
        self.info_text()

        # top message
        top_msg = f'Choosing for Player {self.player_counter + 1}...'
        text_surf = self.player_font.render(top_msg, False, 'white')
        text_rect = text_surf.get_rect(midtop=(self.info_rect.midtop[0], s.MARGIN * 2))
        self.display_surf.blit(text_surf, text_rect)

        # bottom message
        text_surf = self.player_font.render(self.bottom_msg, False, 'white')
        text_rect = text_surf.get_rect(midtop=(self.info_rect.midbottom[0], self.info_rect.midbottom[1] + 2 * s.MARGIN))
        self.display_surf.blit(text_surf, text_rect)

    def char_display(self, portrait, selected:bool):
        self.display_surf.blit(portrait.image, portrait.rect)

        if selected:
            pygame.draw.rect(self.display_surf, 'white', portrait.rect, 4, 0)

    def info_window(self):
        # get character object
        char_obj = self.char_deck.obj_dict[self.portrait_list[self.index]]

        # get window color
        self.panel_color = s.PANEL_COLORS[char_obj.color]

        # create info window
        self.info_rect = pygame.Rect((s.POSITIONS['roller']), (self.window_width, self.window_height))
        pygame.draw.rect(self.display_surf, self.panel_color, self.info_rect, border_radius=12)

    def info_text(self):
        char_obj = self.char_deck.obj_dict[self.portrait_list[self.index]]

        self.text_top = self.info_rect.top + s.MARGIN

        # character info
        self.display_single_info_line(char_obj.name, self.title_font)
        self.display_single_info_line(f'Age: {char_obj.age}', self.font)
        self.display_single_info_line(f'Birthday: {char_obj.birthday}', self.font)
        self.display_single_info_line(f'Hobbies: {char_obj.hobbies}', self.font)
        self.display_single_info_line(char_obj.fact, self.font)

        # bio
        self.text_top += s.LINE_SPACE
        for line in textwrap.wrap(char_obj.bio, self.window_width_chars):
            text_surf = self.font.render(line, False, 'white')
            text_rect = text_surf.get_rect(topleft=(self.info_rect.left + s.MARGIN, self.text_top))
            self.display_surf.blit(text_surf, text_rect)
            self.text_top += text_surf.get_height()

        # traits
        #TODO: figure out how to show base trait position / value somehow
        self.text_top += s.MARGIN
        self.display_single_info_line('Traits:', self.title_font)
        self.display_single_info_line(f'Speed: {char_obj.speed_scale}', self.font)
        self.display_single_info_line(f'Might: {char_obj.might_scale}', self.font)
        self.display_single_info_line(f'Knowledge: {char_obj.knowledge_scale}', self.font)
        self.display_single_info_line(f'Sanity: {char_obj.sanity_scale}', self.font)

    def display_single_info_line(self, text:str, font:pygame.font.Font):

        text_surf = font.render(text, False, 'white')
        text_rect = text_surf.get_rect(topleft=(self.info_rect.left + s.MARGIN, self.text_top))
        self.display_surf.blit(text_surf, text_rect)
        self.text_top += text_surf.get_height()

        self.text_top += s.LINE_SPACE

    def select_char(self, char_name:str):
        self.selected_chars.append(char_name)

        selected_color = self.char_deck.obj_dict[char_name].color

        for i, character in enumerate(self.char_deck.obj_dict.values()):
            if character.color == selected_color:
                self.portrait_dict[character.name].image = self.portrait_dict[character.name].img_bw
                self.portrait_dict[character.name].chosen = True


    def input(self):
        keys = pygame.key.get_pressed()

        current_selection = self.portrait_list[self.index]

        if not self.timer.active:
            if keys[pygame.K_UP]:
                self.index -= 2
                self.timer.activate()

            if keys[pygame.K_DOWN]:
                self.index += 2
                self.timer.activate()

            if keys[pygame.K_LEFT]:
                self.index -= 1
                self.timer.activate()

            if keys[pygame.K_RIGHT]:
                self.index += 1
                self.timer.activate()

            if keys[pygame.K_RETURN]:
                self.timer.activate()
                if self.portrait_dict[current_selection].chosen:
                    self.bottom_msg = 'Character taken. Select a different character'
                else:
                    self.select_char(current_selection)
                    print(self.selected_chars)
                    self.player_counter += 1
                    self.bottom_msg = '[Press Enter to select this character]'

        # TODO: skip already slected characters / otherwise make them unselectable

        # clamp values
        if self.index < 0:
            self.index = len(self.char_deck.name_list) - 1
        if self.index > len(self.char_deck.name_list) - 1:
            self.index = 0

    def update(self):
        self.display()
        self.input()
        self.timer.update()


class Portrait():
    def __init__(self, char_name:str, x:int, y:int):
        self.name = char_name

        self.x = x
        self.y = y

        self.image_name = self.name.lower().replace(' ', '_').replace('.', '').replace("'", '').replace(',', '')

        # color image
        self.img_color = pygame.image.load(f'../graphics/characters/portraits/{self.image_name}.png').convert_alpha()
        self.img_color = pygame.transform.scale(self.img_color, s.PORTRAIT_SIZE)

        # B&W image
        self.img_bw = pygame.image.load(f'../graphics/characters/portraits/{self.image_name}_bw.png').convert_alpha()
        self.img_bw = pygame.transform.scale(self.img_bw, s.PORTRAIT_SIZE)

        self.image = self.img_color
        self.rect = self.image.get_rect(topleft=(x, y))

        self.chosen = False

    def set_img_bw(self):
        self.image = self.img_bw
