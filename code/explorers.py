import pygame
import settings as s
from timer import Timer


class Explorer(pygame.sprite.Sprite):
    def __init__(self, char_info) -> None:
        super().__init__()

        # character info
        self.char_name = char_info['name']
        self.color = char_info['color']
        self.age = char_info['age']
        self.birthday = char_info['birthday']
        self.hobbies = char_info['hobbies']
        self.fact = char_info['fact']
        self.bio = char_info['bio']

        # images
        image_name = self.char_name.lower().replace(' ', '_').replace('.', '').replace("'", '').replace(',', '')

        self.image = pygame.image.load(f'../graphics/characters/{image_name}.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (s.CHAR_SIZE, s.CHAR_SIZE))

        self.layer = s.LAYERS['players']

        # traits
        self.speed_scale = char_info['speed scale']
        self.speed_base_pos = char_info['base speed pos']
        self.speed_pos = self.speed_base_pos

        self.might_scale = char_info['might scale']
        self.might_base_pos = char_info['base might pos']
        self.might_pos = self.might_base_pos

        self.knowledge_scale = char_info['knowledge scale']
        self.knowledge_base_pos = char_info['base knowledge pos']
        self.knowledge_pos = self.knowledge_base_pos

        self.sanity_scale = char_info['sanity scale']
        self.sanity_base_pos = char_info['base sanity pos']
        self.sanity_pos = self.sanity_base_pos

    def init_player(self, pos: tuple, group):
        # TODO: run when a player chooses a character
        # TODO: associate a player with a character
        self.set_pos(pos)
        group.add(self)

    def set_pos(self, grid_pos: tuple):
        self.grid_pos = grid_pos
        # TODO: figure out how to do this in terms of rect x and y?
        self.pos = (self.grid_pos[0] * s.TILE_SIZE + s.TILE_SIZE//2, self.grid_pos[1] * s.TILE_SIZE + s.TILE_SIZE//2)
        self.rect = self.image.get_rect(center=self.pos)

    def trait_roll(self):
        pass

    def update(self,dt):
        pass