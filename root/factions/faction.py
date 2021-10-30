from abc import ABC, abstractmethod
from typing import List, Set
import numpy as np
from collections import Counter


class Faction(ABC):
    def __init__(self):
        self.hand = []
        self.score = 0
        self.crafted_items = []
        self.crafted_cards = []

        self.building_clearing = {}
        self.warriors_clearing = Counter()


    @abstractmethod
    def setup(self) -> List[Set]:
        pass

    @abstractmethod
    def birdsong(self) -> List[Set]:
        pass

    @abstractmethod
    def daylight(self) -> List[Set]:
        pass

    @abstractmethod
    def evening(self) -> List[Set]:
        pass

    def move(self, clearing_from, clearing_to):
        pass

    def can_move_from(self) -> Set:
        pass

    def can_move_to(self, clearing_from) -> Set:
        pass

    def pre_battle(self):

    def battle(self, clearing, faction):
        faction.pre_battle(self)
        if (num_warriors := self.warriors_clearing[clearing]) > 0:
            d1, d2 = np.random.randint(3, size=2)
            if d2 > d1:
                d1, d2 = d2, d1
            self_attack = min(d1, num_warriors)

    def post_battle(self, faction):
        pass

    def can_battle(self, clearing):
        pass

    @abstractmethod
    def craft(self, card) -> Set:
        pass


