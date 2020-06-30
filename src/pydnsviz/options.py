import typing


class TsigKey:
    def __init__(self):
        self.name: typing.Optional[str] = None
        self.data: typing.Optional[str] = None


class DnsHost:
    def __init__(self):
        self.host: typing.Optional[str] = None
        self.port: int = 53


class Zone:
    def __init__(self):
        self.name: typing.Optional[str] = None


class ZoneAxfr(Zone):
    def __init__(self):
        super().__init__()
        self.host: DnsHost = DnsHost()
        self.key: TsigKey = TsigKey()


class ZoneFile(Zone):
    def __init__(self):
        super().__init__()
        self.file: typing.Optional[str] = None


class Options:
    def __init__(self):
        self.zones: typing.List[Zone] = []
        self.last_key: typing.Optional[TsigKey] = None
        self.last_host: DnsHost = DnsHost()
