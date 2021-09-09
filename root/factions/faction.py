from abc import ABC, abstractmethod
from typing import List, Set


class Faction(ABC):
    def __init__(self):
        self.hand = []
        self.score = 0
        self.crafted_items = []
        self.crafted_cards = []

    @abstractmethod
    def stepup(self) -> List[Set]:
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
