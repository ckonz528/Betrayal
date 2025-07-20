import event_fxns
import string

class Card():
    def __init__(self, card_info: dict) -> None:
        self.name = card_info['name']
        self.description = card_info['description']
        self.action_text = card_info['action_text']


class ObjectCard(Card):
    def __init__(self, card_info: dict, obj_type: str) -> None:
        super().__init__(card_info)
        self.weapon = card_info['weapon']
        self.type = obj_type

class EventCard(Card):
    def __init__(self, card_info: dict) -> None:
        super().__init__(card_info)

        # self.result_text = card_info['result_text']

        # attach the event function to the card
        try:
            fxn_name = self.name.translate(str.maketrans('', '', string.punctuation)).lower().replace(" ","_")
            self.event_fxn = getattr(event_fxns, fxn_name)
        except:
            self.event_fxn = None