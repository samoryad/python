from abc import ABC, abstractmethod


class Clothes(ABC):
    @abstractmethod
    def fabric_consumption(self):
        pass


class Coat(Clothes):
    def __init__(self, size):
        self.size = size

    @property
    def fabric_consumption(self):
        return round(self.size / 6.5 + 0.5, 3)


class Suit(Clothes):
    def __init__(self, height):
        self.height = height

    @property
    def fabric_consumption(self):
        return 2 * self.height + 0.3


c = Coat(54)
print(c.fabric_consumption)
s = Suit(180)
print(s.fabric_consumption)
print(c.fabric_consumption + s.fabric_consumption)
