import json


class Character():
    def __init__(self, char_info) -> None:
        # character info
        self.char_name = char_info['name']
        self.color = char_info['color']
        self.age = char_info['age']
        self.birthday = char_info['birthday']
        self.hobbies = char_info['hobbies']
        self.fact = char_info['fact']
        self.bio = char_info['bio']

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
