import math
import time

import attr
from colour import Color
import numpy as np

from .base import BaseEffect


@attr.s(auto_attribs=True)
class Wander(BaseEffect):
    name: str = attr.ib(default="WANDER")
    wander_center: np.array = attr.ib(default=np.array([0.5, 0.5]))

    def on_tick(self) -> None:
        self.wander_center += np.random.normal(0, 0.01, 2)
        self.wander_center = np.clip(self.wander_center, -1, 1)

    def calculate_zone_color(self, zone):
        dist = np.linalg.norm(self.wander_center - zone.center)

        hue = math.sin(dist * 1.5) - time.time() / 4

        return Color(hsl=(hue, 1, 0.5))


effect = Wander
