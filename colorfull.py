#!/usr/bin/env python3
import colorsys
import math
import time
import random

import numpy as np

from devices import get_device
from effects import get_effect

device = get_device("lifx_tile")
effect = get_effect("spectrum")


while True:
    device.set_effect(effect)
    time.sleep(1 / 60)
