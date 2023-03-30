from network import extract_ip_addr
import netifaces


class NetworkInterfaces:
    def __init__(self):
        interfaces = netifaces.interfaces()
        self._inter = self._read_all_interfaces(interfaces)

    @staticmethod
    def _read_all_interfaces(interfaces):
        data = {}
        for interface in interfaces:
            families = netifaces.ifaddresses(interface)
            for _, family in families.items():
                for item in family:
                    data[item['addr']] = item
        return data

    def __getitem__(self, item):
        return self._inter[item]


ip = extract_ip_addr()
network_interfaces = NetworkInterfaces()
print(network_interfaces[ip])