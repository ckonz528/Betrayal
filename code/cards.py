class Card():
    def __init__(self, card_info: dict) -> None:
        self.name = card_info['name']
        self.description = card_info['description']
        self.action = card_info['action']


class ObjectCard(Card):
    def __init__(self, card_info: dict, obj_type: str) -> None:
        super().__init__(card_info)
        self.weapon = card_info['weapon']
        self.type = obj_type
