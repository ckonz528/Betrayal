import json
from random import shuffle
from rooms import Room
import cards
from explorers import Explorer
from typing import cast, Generic, TypeVar

T = TypeVar('T')
class Deck(Generic[T]):
    def __init__(self, info_path: str, object: str, messenger: object = None, obj_type: str | None = None) -> None:
        # construct deck of tiles
        with open(info_path, "r", encoding='utf-8') as data_file:
            info_list = json.load(data_file)

        self.obj_dict: dict[str, T]

        # choose what type of card objects are created
        if object == 'object':
            assert obj_type is not None
            self.obj_dict = {card_info['name']: cast(T, cards.ObjectCard(card_info, obj_type)) for card_info in info_list}
        elif object == 'event':
            self.obj_dict = {card_info['name']: cast(T, cards.EventCard(card_info)) for card_info in info_list}
        elif object == 'room':
            self.obj_dict = {card_info['name']: cast(T, Room(card_info, messenger)) for card_info in info_list}
        elif object == 'explorer':
            self.obj_dict = {card_info['name']: cast(T, Explorer(card_info)) for card_info in info_list}

        self.name_list = list(self.obj_dict.keys())

        # shuffle deck after importing and creating card objs
        self.shuffle_deck()

    def shuffle_deck(self):
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


class RoomDeck(Deck[Room]):
    def __init__(self, info_path: str, object: str, messenger: object) -> None:
        super().__init__(info_path, object, messenger)

    def choose_card(self, floor):
        # draw tiles in order of "stack"
        for chosen_tile in self.name_list:
            tile = self.obj_dict[chosen_tile]

            # check if the tile can be placed in the current floor
            if floor in tile.floors:
                self.name_list.remove(chosen_tile)
                return tile

        assert False, "Room not found??"

        # TODO: add logic for if there are no more tiles for that floor
