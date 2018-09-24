from abc import ABC, abstractmethod

import attr

@attr.s(auto_attribs=True)
class BaseDevice(ABC):
    name: str

    @abstractmethod
    def set_all(self, color) -> None:
        pass
