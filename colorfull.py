import colorsys
import math
import time
import random

import numpy as np

from devices.devices import devices
from effects.effects import effects

ork = devices["OpenRazerKeyboard"]
wander = effects["Wander"]



def spectrum(x, y):
    t = time.time()

    hue = x + y / 5 + t / 3
    hue %= 1

    color = list(map(lambda x: x * 255, colorsys.hsv_to_rgb(hue, 1, 1)))

    # return (x * 255, y * 255, (t * 255) % 255)
    return color




while True:
    # ork.set_func(spectrum)
    # ork.set_func(wander)
    ork.set_effect(wander)
    time.sleep(1 / 60)
