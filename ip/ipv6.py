from ip import Ip

class Ipv6(Ip):

    _delimiter = ':'
    # technically speaking there is no global broadcast, need to find a better
    # term for this.
    GLOBAL_BROADCAST = Ipv6("FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF")

    @property
    def address(self):
        return super(Ipv6, self).address()

    @address.setter
    def address(self, address):
        def list_addr(addr):
            if len(addr) != 8:
                raise ValueError('Expected 8 octet address, got %i in (%s)' %
                                 (len(addr), address))
            # converts a list into a single long
            _addr = 0
            #for octet in range(4):
                #_addr += addr[octet] * 2 ** (8 * (3 - octet))
            #return _addr
            #eww copy paste
            pass

        def string_addr(addr):
            pass

        if isinstance(address, str):
            self._address = string_addr(address)
        elif isinstance(address, tuple) or isinstance(address, list):
            self._address = list_addr(address)
        elif isinstance(address, int) or isinstance(address, long):
            self._address = address
        elif isinstance(address, Ipv6):
            self._address = list_addr(list(address))
        else:
            raise TypeError(
                'Unsupported type for address initialization %s, (%s)' % (
                    type(address), address)
                )
        pass


    def _hex_digit(self, digit):
        # >>> hex(65535)[2:].rjust(4,'0')
        # 'ffff'
        return hex(digit)[2:].rjust(4,'0')


    def _dec_digit(self, digit):
        # this seems silly
        return digit


    def __init__(self, address):
        super(Ipv6, self).__init__(address)


    def __repr__(self):
        return "%s('%s')" %("Ipv6", str(self))


    def __str__(self):
        # should probably implement shorthand version, probably in a seperate
        # funcion
        return self._delimiter.join(
            map(self._hex_digit, tuple(self))
            )


    def __iter__(self):
        pass


    def __getitem__(self, index):
        return tuple(self)[index]


    def __add__(self, other):
        return Ipv6(self.address + other)


    def __sub__(self, other):
        return Ipv6(self.address - other)


    def __and__(self, other):
        return Ipv6(self.address & other)


    def __rand__(self, other):
        return self.address & other


    def __or__(self, other):
        return Ipv6(self.address | other)


    def __ror__(self, other):
        return self.address | other


    def __xor__(self, other):
        return Ipv6(self.address ^ other)


    def __rxor__(self, other):
        return self.address ^ other


    def __invert__(self):
        return Ipv6(self ^ self.GLOBAL_BROADCAST)

__all__ = ['Ipv6']
