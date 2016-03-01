from ip import Ip

class Ipv4(Ip):

    _delimiter = '.'

    @property
    def address(self):
        return super(Ipv4, self).address

    @address.setter
    def address(self, address):
        def list_addr(addr):
            if len(addr) != 4:
                raise ValueError('Expected 4 octet address, got %i in (%s)' %
                                 (len(addr), address))
            # converts a list into a single long
            # [255, 255, 255, 255] -> 0b11111111 11111111 11111111 11111111
            _addr = 0
            for octet in range(4):
                _addr += addr[octet] * 2 ** (8 * (3 - octet))
            return _addr

        def string_addr(addr):
            return list_addr(
                map(int, addr.split(self._delimiter))
                )

        if type(address) == str:
            self._address = string_addr(address)
        elif type(address) == tuple or type(address) == list:
            self._address = list_addr(address)
        elif type(address) == int or type(address) == long:
            self._address = address
        else:
            raise NotImplemented(
                'Unsupported type for address initialization %s, (%s)' %(
                    type(address), address)
                )


    def __init__(self, address):
        super(Ipv4, self).__init__(address)


    def __repr__(self):
        return "%s('%s')" % ("Ipv4", str(self))


    def __str__(self):
        return ".".join(map(str,tuple(self)))


    def __iter__(self):
        # converts an int to a list
        # 0b11111111 11111111 11111111 11111111 -> [255, 255, 255, 255]
        addr = []
        for i in range(4):
            addr += [255 & self.address >> (8 * (3 - i))]
        return iter(map(int, addr))


    def __index__(self, index):
        return tuple(self)[index]


    def __add__(self, other):
        return Ipv4(self.address + other)


    def __sub__(self, other):
        return Ipv4(self.address - other)


    def __and__(self, other):
        return Ipv4(self.address & other)


    def __or__(self, other):
        return Ipv4(self.address | other)


    def __xor__(self, other):
        return Ipv4(self.address ^ other)


__all__ = ['Ipv4']