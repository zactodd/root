from abc import ABC, abstractmethod


class Item(ABC):
    def __init__(self):
        self.is_exhausted = False
        self.is_damaged = False

    @abstractmethod
    def actions(self):
        pass
