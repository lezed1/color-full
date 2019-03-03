import attr
from .base import BaseDevice

@attr.s(auto_attribs=True)
class Dummy(BaseDevice):
    name: str = attr.ib(default="DUMMY")

    def set_all(self, color):
        print(color)


Device = Dummy
