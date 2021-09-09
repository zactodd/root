from root.cards.suit import Suit
from root.items.item import Item
from collections import Counter
import operator
from typing import List


class Clearing:
    def __init__(self, idx: int, suit: Suit, num_build_slots: int, ruin_items: List[Item]=None) -> None:
        self.idx = idx
        self.suit = suit
        if ruin_items is None:
            self.build_slots = [None] * num_build_slots
            self.has_ruin = False
        else:
            self.build_slots = [None] * (num_build_slots - 1) + [ruin_items]
            self.has_ruin = True

        self.warriors = Counter()
        self.building = Counter()

        self.ruler = None

    def update_ruler(self) -> None:
        # TODO handle ties
        return max((self.warriors + self.building).items(), key=operator.itemgetter(1))[0]

    def move_in(self, faction, num_warriors) -> None:
        self.warriors[faction] += num_warriors

    def move_out(self, faction, num_warriors) -> None:
        assert self.warriors[faction] - num_warriors >= 0, \
            "There are less warriors in clearing that you are asking to move."
        self.warriors[faction] -= num_warriors
