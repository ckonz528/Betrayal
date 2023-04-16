import json
from random import shuffle
from rooms import Room


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


class Deck():
    def __init__(self, info_path: str, object: str) -> None:
        # construct deck of tiles
        with open(info_path, "r", encoding='utf-8') as data_file:
            info_list = json.load(data_file)

        # choose what type of card objects are created
        if object == 'object':
            self.obj_dict = {card_info['name']: ObjectCard(
                card_info) for card_info in info_list}
        elif object == 'event':
            self.obj_dict = {card_info['name']: Card(
                card_info) for card_info in info_list}
        elif object == 'room':
            self.obj_dict = {card_info['name']: Room(
                card_info) for card_info in info_list}

        self.name_list = list(self.obj_dict.keys())

        # shuffle deck after importing and creating card objs
        self.shuffle()

    def shuffle(self):
        return shuffle(self.name_list)

    def choose_card(self, **kwargs):
        # draw cards in order of "stack", get card object
        chosen_card = self.name_list[0]
        card_obj = self.obj_dict[chosen_card]

        # remove drawn card from stack
        self.name_list.remove(chosen_card)

        return card_obj


if __name__ == '__main__':
    omen_deck = Deck('../data/omens.json', 'object')
    omen_card = omen_deck.choose_card()
    print(omen_card.name)
    print(omen_card.weapon)

    item_deck = Deck('../data/items.json', 'object')
    item_card = item_deck.choose_card()
    print(item_card.name)
    print(item_card.weapon)

    event_deck = Deck('../data/events.json', 'event')
    event_card = event_deck.choose_card()
    print(event_card.name)
    print(event_card.description)
    print(event_card.action)
