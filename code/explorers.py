import pygame
import settings as s
from timer import Timer


class Explorer(pygame.sprite.Sprite):
    def __init__(self, char_info) -> None:
        super().__init__()

        # character info
        self.name = char_info['name']
        self.color = char_info['color']
        self.age = char_info['age']
        self.birthday = char_info['birthday']
        self.hobbies = char_info['hobbies']
        self.fact = char_info['fact']
        self.bio = char_info['bio']

        # images
        image_name = self.name.lower().replace(' ', '_').replace('.', '').replace("'", '').replace(',', '')

        self.image = pygame.image.load(f'../graphics/characters/tokens/{image_name}.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (s.CHAR_SIZE, s.CHAR_SIZE))

        # traits
        self.speed_scale = char_info['speed scale']
        self.speed_base_pos = char_info['base speed pos']
        self.speed_pos = self.speed_base_pos
        # self.speed = self.speed_scale[self.speed_pos]

        self.might_scale = char_info['might scale']
        self.might_base_pos = char_info['base might pos']
        self.might_pos = self.might_base_pos
        # self.might = self.might_scale[self.might_pos]

        self.knowledge_scale = char_info['knowledge scale']
        self.knowledge_base_pos = char_info['base knowledge pos']
        self.knowledge_pos = self.knowledge_base_pos
        # self.knowledge = self.knowledge_scale[self.knowledge_pos]

        self.sanity_scale = char_info['sanity scale']
        self.sanity_base_pos = char_info['base sanity pos']
        self.sanity_pos = self.sanity_base_pos
        # self.sanity = self.sanity_scale[self.sanity_pos]

        self.traits = {'speed': self.speed_scale[self.speed_pos],
                       'might': self.might_scale[self.might_pos],
                       'knowledge': self.knowledge_scale[self.knowledge_pos],
                       'sanity': self.sanity_scale[self.sanity_pos]}

        # inventory
        self.inventory = {}

        # game attributes
        self.layer = s.LAYERS['players']
        self.direction = pygame.math.Vector2()
        self.floor: str = 'ground'
        self.allow_move = False

        # player life status
        self.dead = False

    def set_pos(self, grid_pos: tuple):
        self.grid_pos = grid_pos
        # TODO: figure out how to do this in terms of rect x and y?
        self.pos = (self.grid_pos[0] * s.TILE_SIZE + s.TILE_SIZE//2, self.grid_pos[1] * s.TILE_SIZE + s.TILE_SIZE//2)
        self.rect = self.image.get_rect(center=self.pos)

    def adjust_pos(self, direction):
        self.pos = (self.grid_pos[0] * s.TILE_SIZE + s.TILE_SIZE//2, self.grid_pos[1] * s.TILE_SIZE + s.TILE_SIZE//2)
        if direction == "NW":
            self.pos = (self.pos[0] - s.CHAR_SIZE, self.pos[1] - s.CHAR_SIZE)
        elif direction == "N":
            self.pos = (self.pos[0], self.pos[1] - s.CHAR_SIZE)
        elif direction == "NE":
            self.pos = (self.pos[0] + s.CHAR_SIZE, self.pos[1] - s.CHAR_SIZE)
        elif direction == "E":
            self.pos = (self.pos[0] + s.CHAR_SIZE, self.pos[1])
        elif direction == "SE":
            self.pos = (self.pos[0] + s.CHAR_SIZE, self.pos[1] + s.CHAR_SIZE)
        elif direction == "S":
            self.pos = (self.pos[0], self.pos[1] + s.CHAR_SIZE)
        elif direction == "SW":
            self.pos = (self.pos[0] - s.CHAR_SIZE, self.pos[1] + s.CHAR_SIZE)
        elif direction == "W":
            self.pos = (self.pos[0] - s.CHAR_SIZE, self.pos[1])

        self.rect = self.image.get_rect(center=self.pos)

    def add_item(self, item: object):
        self.inventory[item.name] = item

    def adjust_stat(self, stat:str, amnt:int):
        '''
        Adjusts a player stat by specified ammount
        '''
        # get current stat info
        stat_pos = f'{stat}_pos'
        stat_scale = f'{stat}_scale'

        len_scale = len(getattr(self, stat_scale))

        # adjust stat
        if getattr(self, stat_pos) + amnt >= len_scale:
            setattr(self, stat_pos, len_scale)
        elif getattr(self, stat_pos) + amnt <= 0:
            setattr(self, stat_pos, 0)
            self.dead = True        
        else:
            setattr(self, stat_pos, getattr(self, stat_pos) + amnt)
        
        # update trait dictionary
        self.traits[stat] = stat_scale[stat_pos]

        #TODO: add message indicating stat change


    def update(self,dt):
        pass