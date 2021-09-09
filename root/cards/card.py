from abc import ABC, abstractmethod
from root.cards.suit import Suit
from typing import List


class Card(ABC):
    @property
    @abstractmethod
    def crafting_requirements(self) -> List[Suit]:
        pass

    @abstractmethod
    def actions(self, faction) -> None:
        pass

    @property
    @abstractmethod
    def suit(self) -> Suit:
        pass

