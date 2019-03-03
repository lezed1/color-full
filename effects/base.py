from abc import ABC, abstractmethod

import attr
from colour import Color


@attr.s(auto_attribs=True)
class BaseEffect(ABC):
    name: str

    def on_tick(self) -> None:
        pass

    @abstractmethod
    def calculate_zone_color(self, zone) -> Color:
        pass
