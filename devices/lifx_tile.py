import attr
from lifxlan import LifxLAN
import numpy as np

from .base import BaseDevice
from .shared import Zone

num_expected_lights = 1
lifx = LifxLAN(num_expected_lights)

tile_chain = lifx.get_tilechain_lights()[0]
cols, rows = tile_chain.get_canvas_dimensions()


@attr.s(auto_attribs=True)
class LifxTile(BaseDevice):
    name: str = attr.ib(default="LIFX Tile")

    def set_all(self, color):
        print(color)

    def set_effect(self, effect):
        effect.on_tick()

        background_colors = []
        for row in range(rows):
            color_row = []
            for col in range(cols):
                center = np.array([row / rows, col / cols])
                zone = Zone((row, col), center)
                color = effect.calculate_zone_color(zone)
                lifx_color = (*map(lambda x: int(x * 65535) % 65536,
                                   color.hsl), 4900)
                color_row.append(lifx_color)
            background_colors.append(color_row)

        tile_chain.project_matrix(background_colors, 1000)


device = LifxTile
