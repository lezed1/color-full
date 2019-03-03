import importlib
from .base import BaseDevice


def get_device(name) -> BaseDevice:
    return importlib.import_module(__name__ + "." + name).device()
