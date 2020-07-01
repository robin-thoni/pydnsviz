import graphviz
import typing

import dns.rdtypes.ANY.SOA
import dns.rdtypes.ANY.CNAME
import dns.rdtypes.ANY.NS
import dns.rdtypes.ANY.MX
import dns.rdtypes.ANY.TXT
import dns.rdtypes.ANY.SPF
import dns.rdtypes.IN.A
import dns.rdtypes.IN.AAAA
import dns.rdtypes.IN.SRV
import dns.zone


def map_zones(zones: typing.List[dns.zone.Zone], dot: graphviz.Digraph, record_filter: typing.Callable = None):
    for zone in zones:
        for (name, node) in zone.nodes.items():
            for rdataset in node.rdatasets:
                for record in rdataset.items:
                    if not record_filter or record_filter(zone, name, node, rdataset, record, dot):
                        if isinstance(record, dns.rdtypes.ANY.SOA.SOA):
                            dot.edge(name.to_text(), record.mname.to_text(), 'SOA')
                        elif isinstance(record, dns.rdtypes.IN.A.A):
                            dot.edge(name.to_text(), record.to_text(), 'A')
                        elif isinstance(record, dns.rdtypes.IN.AAAA.AAAA):
                            dot.edge(name.to_text(), record.to_text(), 'AAAA')
                        elif isinstance(record, dns.rdtypes.ANY.CNAME.CNAME):
                            dot.edge(name.to_text(), record.to_text(), 'CNAME')
                        elif isinstance(record, dns.rdtypes.ANY.NS.NS):
                            dot.edge(name.to_text(), record.to_text(), 'NS')
                        elif isinstance(record, dns.rdtypes.ANY.MX.MX):
                            dot.edge(name.to_text(), record.exchange.to_text(), 'MX')
                        elif isinstance(record, dns.rdtypes.ANY.TXT.TXT):
                            pass  # TODO extract spf MX
                        elif isinstance(record, dns.rdtypes.ANY.SPF.SPF):
                            pass  # TODO extract spf MX
                        elif isinstance(record, dns.rdtypes.IN.SRV.SRV):
                            dot.edge(name.to_text(), record.target.to_text(), 'SRV')
                        else:
                            print('Not handled:', record)
