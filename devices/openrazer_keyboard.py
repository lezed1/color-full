# This hasn't been updated or tested in a while :(
import attr
from openrazer.client import DeviceManager
import numpy as np

from . import ork_temp_map as maps

from .base import BaseDevice
from .shared import Zone

device_manager = DeviceManager()
keyboard = device_manager.devices[0]


@attr.s(auto_attribs=True)
class OpenrazerKeyboard(BaseDevice):
    name: str = attr.ib(default="OPENRAZER")

    def set_all(self, color):
        for r in range(keyboard.fx.advanced.rows):
            for c in range(keyboard.fx.advanced.cols):
                keyboard.fx.advanced.matrix.set(r, c, color)

        keyboard.fx.advanced.draw()

    def set_zone(self, name, color):
        keyboard.fx.advanced.matrix.set(*name, list(map(int, color)))

    def sync(self):
        keyboard.fx.advanced.draw()

    def set_func(self, func):
        for name, loc in maps.location_map.items():
            zone = maps.keymap[name]
            loc = (loc[0][0] + loc[1][0]) / 2 / 736, (
                loc[0][1] + loc[1][1]) / 2 / 274
            # loc = (loc[0][0] + loc[1][0]) / 2/ 736, (loc[0][1] + loc[1][1]) / 2 / 736
            self.set_zone(zone, func(*loc))

        keyboard.fx.advanced.draw()

    def set_effect(self, effect):
        effect.on_tick()

        for name, loc in maps.location_map.items():
            zone = maps.keymap[name]
            center = np.array([(loc[0][0] + loc[1][0]) / 2 / 736,
                               (loc[0][1] + loc[1][1]) / 2 / 274])
            z_for_effect = Zone(name, center)
            self.set_zone(zone, effect.calculate_zone_color(z_for_effect))

        keyboard.fx.advanced.draw()


device = OpenrazerKeyboard
