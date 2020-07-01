#! /usr/bin/env python3

import sys

import dns.query
import dns.zone
import dns.tsigkeyring

import argparse

import graphviz

import pydnsviz.core.argparseactions
import pydnsviz.core.options
import pydnsviz.core.mapper


def main(argv):
    options = pydnsviz.core.options.Options()

    parser = argparse.ArgumentParser(description='Visualize DNS zones')

    # parser.add_argument('--record-filter', metavar='FILTER', type=str, help='Filter records to be included')

    parser.add_argument('--zone-axfr', metavar='ZONE', type=str, action=pydnsviz.core.argparseactions.ZoneAxfrAction, options=options,
                        help='Load a zone via AXFR')
    parser.add_argument('--zone-axfr-host', metavar='HOST', type=str, action=pydnsviz.core.argparseactions.ZoneAxfrHostAction, options=options,
                        help='Set the hostname or IP for the DNS server for the subsequents --zone-axfr')
    parser.add_argument('--zone-axfr-key', metavar='KEY', type=str, action=pydnsviz.core.argparseactions.ZoneAxfrKeyAction, options=options,
                        help='Set the key for the subsequents --zone-axfr in format `${KEY_NAME}:${KEY_DATA}`')
    parser.add_argument('--zone-axfr-keyfile', metavar='FILE', type=str, action=pydnsviz.core.argparseactions.ZoneAxfrKeyFileAction, options=options,
                        help='Set the path to a file containing a key for the subsequents '
                             '--zone-axfr in format `${KEY_NAME}:${KEY_DATA}`')

    parser.add_argument('--zone-file', metavar='ZONE', type=str, action=pydnsviz.core.argparseactions.ZoneFileAction, options=options,
                        help='Load a zone file')
    parser.add_argument('--zone-file-path', metavar='FILE', type=str, action=pydnsviz.core.argparseactions.ZoneFilePathAction, options=options,
                        help='Set the zone file path the the previous --zone-file')

    args = parser.parse_args(argv[1:])

    # record_filter_str = args.record_filter
    #
    # if record_filter_str:
    #     record_filter = eval('lambda zone, name, node, rdataset, record, dot: ' + record_filter_str)
    # else:
    #     record_filter = None

    zones = []
    for zone in options.zones:
        if isinstance(zone, pydnsviz.core.argparseactions.ZoneAxfr):
            mykeyring = dns.tsigkeyring.from_text({
                zone.key.name: zone.key.data
            }) if zone.key else None
            xfr = dns.query.xfr(zone.host.host, zone.name, port=zone.host.port, keyring=mykeyring, relativize=False)
            z = dns.zone.from_xfr(xfr, relativize=False)
        elif isinstance(zone, pydnsviz.core.argparseactions.ZoneFile):
            with open(zone.file, 'r') as f:
                z = dns.zone.from_file(f, zone.name, relativize=False)
        zones.append(z)

    dot = graphviz.Digraph(comment='DNS')
    pydnsviz.core.mapper.map_zones(zones, dot)
    print(dot.source)


def entrypoint():
    sys.exit(main(sys.argv))


if __name__ == '__main__':
    sys.exit(main(sys.argv))
