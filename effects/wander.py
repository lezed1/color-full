import colorsys
import math
import random
import time

import attr
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
        hue %= 1

        color = list(map(lambda x: x * 255, colorsys.hsv_to_rgb(hue, 1, 1)))

        return color
