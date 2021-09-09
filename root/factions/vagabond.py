from root.factions.faction import Faction
from abc import ABC, abstractmethod

class Vagabon(Faction):
    def __init__(self):
        self.items = []


class VBCLass(ABC):
    @property
    @abstractmethod
    def initial_items(self):
        pass

    @abstractmethod
    def torch(self) -> None:
        pass


# class Tinker