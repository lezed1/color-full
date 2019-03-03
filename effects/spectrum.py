import time

import attr
from colour import Color

from .base import BaseEffect


@attr.s(auto_attribs=True)
class Wander(BaseEffect):
    name: str = attr.ib(default="Spectrum")
    time: float = attr.ib(default=time.time())

    def on_tick(self) -> None:
        self.time = time.time()

    def calculate_zone_color(self, zone):
        hue = zone.center[0] + zone.center[1] / 5 + self.time / 3

        return Color(hsl=(hue, 1, 0.5))


effect = Wander
