import json
import pygame
import settings as s


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
        image_name = self.char_name.lower().replace(
            ' ', '_').replace('.', '').replace('"', '').replace
        self.image = pygame.image.load(
            f'../graphics/characters/{image_name}.png').convert_alpha()
        self.image = pygame.transform.scale(
            self.image, (s.CHAR_SIZE, s.CHAR_SIZE))

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

    def init_player(self, player_name: str):
        # TODO: run when a player chooses a character
        self.player = player_name
        self.set_pos((0, 0))

    def set_pos(self, new_pos: tuple):
        self.pos = new_pos
        self.rect = self.image.get_rect(topleft=self.pos)

    def trait_roll(self):
        pass
