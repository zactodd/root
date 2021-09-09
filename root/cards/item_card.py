from root.cards.card import Card
from root.items.item import Item
from abc import abstractmethod
from typing import List
from root.cards.suit import Suit


class ItemCard(Card):
    @property
    @abstractmethod
    def earned_vps(self) -> int:
        pass

    @property
    @abstractmethod
    def item(self) -> Item:
        pass

    def actions(self, faction) -> None:
        faction.score += self.earned_vps
        faction.items.append(self.item)


class Boot(ItemCard):
    def crafting_requirements(self) -> List[Suit]:
        return [Suit.MOUSE]

    def earned_vps(self) -> int:
        return 1


class Crossbow(ItemCard):
    def crafting_requirements(self) -> List[Suit]:
        return [Suit.FOX]

    def earned_vps(self) -> int:
        return 1


class Bag(ItemCard):
    def crafting_requirements(self) -> List[Suit]:
        return [Suit.MOUSE]

    def earned_vps(self) -> int:
        return 1


class Sword(ItemCard):
    def crafting_requirements(self) -> List[Suit]:
        return [Suit.FOX] * 2

    def earned_vps(self) -> int:
        return 2


class RootTea(ItemCard):
    def crafting_requirements(self) -> List[Suit]:
        return [Suit.MOUSE]

    def earned_vps(self) -> int:
        return 2


class Hammer(ItemCard):
    def crafting_requirements(self) -> List[Suit]:
        return [Suit.FOX]

    def earned_vps(self) -> int:
        return 2


class Coin(ItemCard):
    def crafting_requirements(self) -> List[Suit]:
        return [Suit.RABBIT]

    def earned_vps(self) -> int:
        return 3



