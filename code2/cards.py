class Card():
    def __init__(self, card_info: dict) -> None:
        # applies to items or omens
        self.name = card_info['name']
        self.description = card_info['description']
        self.action = card_info['action']


class ObjectCard(Card):
    def __init__(self, card_info: dict) -> None:
        super().__init__(card_info)
        self.weapon = card_info['weapon']
