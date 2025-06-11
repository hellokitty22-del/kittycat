

# geo_features.py
from abc import ABC
from dataclasses import dataclass

@dataclass
class Location:
    Y: int = 0
    X: int = 0

    def __str__(self):
        return f"({self.Y},{self.X})"

@dataclass
class Size:
    height: int = 0
    width: int = 0

class GeoFeature(ABC):
    def __init__(self, location: Location, name: str):
        self.location = location
        self.name = name

    def symbol(self):
        return "."

    def get_size(self):
        return 0

class Mountain(GeoFeature):
    def __init__(self, location: Location, name: str, height: int):
        super().__init__(location, name)
        self.height = int(height)

    def symbol(self):
        return "m"

    def __str__(self):
        return f"mountain {self.name}, height {self.height}"

    def get_size(self):
        return self.height

class Lake(GeoFeature):
    def __init__(self, location: Location, name: str, depth: int):
        super().__init__(location, name)
        self.depth = int(depth)

    def symbol(self):
        return "l"

    def __str__(self):
        return f"lake {self.name}, depth {self.depth}"

    def get_size(self):
        return self.depth

class Crater(GeoFeature):
    def __init__(self, location: Location, name: str, perimeter: int):
        super().__init__(location, name)
        self.perimeter = int(perimeter)

    def symbol(self):
        return "c"

    def __str__(self):
        return f"crater {self.name}, perimeter {self.perimeter}"

    def get_size(self):
        return self.perimeter


