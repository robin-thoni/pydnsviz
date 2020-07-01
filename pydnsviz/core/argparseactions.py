import argparse
import re

from pydnsviz.core.options import *


def parse_tsig_key(name_data: str):
    match = re.match(r'([^:]+):([a-zA-Z0-9+/=]+)', name_data)
    if match:
        name = match.group(1)
        data = match.group(2)
        return name, data
    return None


class PyDnsVizAction(argparse.Action):
    def __init__(self, options: Options, option_strings, dest, nargs=None, **kwargs):
        self.options = options
        super(PyDnsVizAction, self).__init__(option_strings, dest, **kwargs)


class ZoneAxfrAction(PyDnsVizAction):
    def __call__(self, parser, namespace, values, option_string=None):
        zone = ZoneAxfr()
        zone.name = values
        zone.host = self.options.last_host
        zone.key = self.options.last_key
        self.options.zones.append(zone)


class ZoneAxfrHostAction(PyDnsVizAction):
    def __call__(self, parser, namespace, values, option_string=None):
        self.options.last_host.host = values


class ZoneAxfrKeyAction(PyDnsVizAction):
    def __call__(self, parser, namespace, values, option_string=None):
        if values == 'none':
            self.options.last_key = None
        else:
            self.options.last_key = TsigKey()
            self.options.last_key.name, self.options.last_key.data = parse_tsig_key(values)


class ZoneAxfrKeyFileAction(PyDnsVizAction):
    def __call__(self, parser, namespace, values, option_string=None):
        with open(values, 'r') as f:
            self.options.last_key = TsigKey()
            self.options.last_key.name, self.options.last_key.data = parse_tsig_key(f.read())


class ZoneFileAction(PyDnsVizAction):
    def __call__(self, parser, namespace, values, option_string=None):
        zone = ZoneFile()
        zone.name = values
        self.options.zones.append(zone)


class ZoneFilePathAction(PyDnsVizAction):
    def __call__(self, parser, namespace, values, option_string=None):
        if self.options.zones:
            zone = self.options.zones[-1]
            if isinstance(zone, ZoneFile):
                zone.file = values
