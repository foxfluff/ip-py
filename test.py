
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

print 'self.address', addr4_1.address, addr4_2.address
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