
#lots of testing

import ip

addr1 = ip.Ip(1234)

print 'self.address', addr1.address
print 'repr        ', repr(addr1)
print 'ip + 5      ', addr1 + 5, type(addr1 + 5)
print 'ip - 5      ', addr1 + 5, type(addr1 - 5)
print

addr4_1 = ip.Ipv4('192.168.0.1')
addr4_2 = ip.Ipv4([172, 16, 0, 1])
addr4_3 = ip.Ipv4((255, 255, 255, 0))

print 'self.address', addr4_1.address, addr4_2.address, addr4_3.address
print 'repr        ', repr(addr4_1), repr(addr4_2)
print 'str         ', str(addr4_1), str(addr4_2)
print 'list        ', list(addr4_1), list(addr4_2)
print 'tuple       ', tuple(addr4_1), tuple(addr4_2)
print 'ip1 + 5     ', addr4_1 + 5, type(addr4_1 + 5)
print 'ip2 + 5     ', addr4_2 + 5, type(addr4_2 + 5)
print 'ip1 - 5     ', addr4_1 - 5, type(addr4_1 - 5)
print 'ip2 - 5     ', addr4_2 - 5, type(addr4_2 - 5)
print 'ip1 | ip2   ', addr4_1 | addr4_2, type(addr4_1 | addr4_2)
print 'ip1 & ip2   ', addr4_1 & addr4_2, type(addr4_1 & addr4_2)
print 'ip1 ^ ip2   ', addr4_1 ^ addr4_2, type(addr4_1 ^ addr4_2)
print 'ip1[0]      ', addr4_1[0]
print 'ip2[0]      ', addr4_2[0]
print '~ip3        ', ~addr4_3
print

addr6_1 = ip.Ipv6('fe20:0:0:0:0:0:0:1')
addr6_2 = ip.Ipv6('fe80::0:1')
addr6_3 = ip.Ipv6('ffff:ffff::0')

print 'self.address', addr6_1.address, addr6_2.address, addr6_3.address
print 'repr        ', repr(addr6_1), repr(addr6_2), repr(addr6_3)
print 'str         ', str(addr6_1), str(addr6_2), str(addr6_3)
print 'list        ', list(addr6_1), list(addr6_2), list(addr6_3)
print 'tuple       ', tuple(addr6_1), tuple(addr6_2), tuple(addr6_3)
print 'ip1 + 5     ', addr6_1 + 5, type(addr6_1 + 5)
print 'ip2 + 5     ', addr6_2 + 5, type(addr6_2 + 5)
print 'ip1 - 5     ', addr6_1 - 5, type(addr6_1 - 5)
print 'ip2 - 5     ', addr6_2 - 5, type(addr6_2 - 5)
print 'ip1 | ip2   ', addr6_1 | addr6_2, type(addr6_1 | addr6_2)
print 'ip1 & ip2   ', addr6_1 & addr6_2, type(addr6_1 & addr6_2)
print 'ip1 ^ ip2   ', addr6_1 ^ addr6_2, type(addr6_1 ^ addr6_2)
print 'ip1[0]      ', addr6_1[0]
print 'ip2[0]      ', addr6_2[0]
print '~ip3        ', ~addr6_3
print
