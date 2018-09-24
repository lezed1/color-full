import attr

@attr.s(auto_attribs=True)
class Zone:
    name: str = attr.ib()
    center: attr.ib()
