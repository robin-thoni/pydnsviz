import typing


class TsigKey:
    def __init__(self):
        self.name: str = None
        self.data: str = None


class DnsHost:
    def __init__(self):
        self.host: str = None
        self.port: int = 53


class Zone:
    def __init__(self):
        self.name: str = None


class ZoneAxfr(Zone):
    def __init__(self):
        self.host: DnsHost = DnsHost()
        self.key: TsigKey = TsigKey()
        super(ZoneAxfr, self)


class ZoneFile(Zone):
    def __init__(self):
        self.file: str = None
        super(ZoneFile, self)


class Options:
    def __init__(self):
        self.zones: typing.List[Zone] = []
        self.last_key: TsigKey = None
        self.last_host: DnsHost = DnsHost()
