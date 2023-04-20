import pygame
import settings as s
import json
from random import shuffle
from rooms import Room
from cards import Card, ObjectCard


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

    def choose_card(self, *args, **kwargs):
        # draw cards in order of "stack", get card object
        chosen_card = self.name_list[0]
        card_obj = self.obj_dict[chosen_card]

        # remove drawn card from stack
        self.remove_card(chosen_card)

        return card_obj

    def get_obj_by_name(self, name: str):
        card_obj = self.obj_dict[name]
        self.remove_card(name)

        return card_obj

    def remove_card(self, card_name: str):
        if card_name in self.name_list:
            self.name_list.remove(card_name)


class RoomDeck(Deck):
    def __init__(self, info_path: str, object: str) -> None:
        super().__init__(info_path, object)

    def choose_card(self, floor):
        # draw tiles in order of "stack"
        for chosen_tile in self.name_list:
            tile = self.obj_dict[chosen_tile]

            # check if the tile can be placed in the current floor
            if floor in tile.floors:
                self.name_list.remove(chosen_tile)
                return tile

        # TODO: add logic for if there are no more tiles for that floor


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

    pygame.init()
    screen = pygame.display.set_mode((s.SCREEN_W, s.SCREEN_H))
    room_deck = Deck('../data/rooms.json', 'room')
    room_tile = room_deck.choose_card(floor='basement')
    print(room_tile.name)
    print(room_tile.instructions)
