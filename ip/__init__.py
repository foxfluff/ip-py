from ip import Ip
from ipv4 import Ipv4
from ipv6 import Ipv6

__name__ = 'ip'
__version__ = '0.3'
__description__ = "Foxfluff's IPv4 and IPv6 datatype handling"
__author__ = 'foxfluff/luma'
__url__ = 'https://github.com/foxfluff'

__all__ = ['Ip', 'Ipv4', 'Ipv6', 'IPV4_LOOPBACK', 'IPV4_GLOBAL_BROADCAST']

IPV4_LOOPBACK = Ipv4([127, 0, 0, 1])
IPV4_GLOBAL_BROADCAST = Ipv4([255, 255, 255, 255])
