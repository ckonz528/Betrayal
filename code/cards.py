import pygame
from pygame.sprite import Sprite
import settings as s
import json
from random import shuffle


class ObjectCard():
    def __init__(self, card_info) -> None:
        self.name = card_info['name']
        self.weapon = card_info['weapon']
        self.description = card_info['description']
        self.action = card_info['action']


class ObjectDeck():
    def __init__(self, json_path) -> None:
        # construct deck
        object_list = json.load(open(json_path))

        self.obj_dict = {card_info['name']: ObjectCard(
            card_info) for card_info in object_list}

        # make a list of cards representing the draw pile
        self.deck = list(self.obj_dict.keys())

        # shuffle deck after creating cards
        self.shuffle()

    def shuffle(self):
        return shuffle(self.deck)

    def draw_card(self):
        pass


if __name__ == '__main__':
    omen_deck = ObjectDeck(s.OMEN_JSON)
    item_deck = ObjectDeck(s.ITEM_JSON)
