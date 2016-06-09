import ip

class Ipv4(ip.Ip):

    # planned/desired features:
    #  - Adding netmask gen/calc/tester (allow for easy error checking for valid
    #    masks, or easy generation of masks using bit count/cidr notation

    @property
    def address(self):
        """Ipv4.address -> return address"""
        return super(Ipv4, self).address

    @address.setter
    def address(self, address, delimiter = "."):
        """Ipv4.address = address
        Assigns address"""
        def list_addr(addr):
            """list_addr(addr)
            Takes a list of digits representing an Ipv4 address and converts
            it to a single long"""
            if len(addr) != 4:
                raise ValueError('Expected 4 octet address, got %i in (%s)' %
                                 (len(addr), address))
            # converts a list into a single long
            # [255, 255, 255, 255] -> 0b11111111 11111111 11111111 11111111
            _addr = 0
            for octet in range(4):
                _addr += addr[octet] << (8 * (3 - octet))
            return _addr

        def string_addr(addr):
            """string_addr(addr)
            Takes a string representing an Ipv6 address, and converts it to a
            single long"""
            return list_addr(
                map(int, addr.split(self._delimiter))
                )

        self._delimiter = delimiter
        if isinstance(address, str):
            self._address = string_addr(address)
        elif isinstance(address, tuple) or isinstance(address, list):
            self._address = list_addr(address)
        elif isinstance(address, int) or isinstance(address, long):
            self._address = address
        elif isinstance(address, Ipv4):
            self._address = list_addr(list(address))
        else:
            raise TypeError(
                'Unsupported type for address initialization %s, (%s)' % (
                    type(address), address)
                )

    def __init__(self, address):
        """Ipv4(address) -> return Ipv4"""
        super(Ipv4, self).__init__(address)

    def __repr__(self):
        """Ipv4.__repr__() <=> repr(Ipv4)"""
        return "%s('%s')" % ("Ipv4", str(self))

    def __str__(self):
        """Ipv4.__str__() <=> str(Ipv4)"""
        return self._delimiter.join(map(str, tuple(self)))

    def __iter__(self):
        """Ipv4.__iter__() <=> iter(Ipv4)"""
        # converts an int to a list
        # 0b11111111 11111111 11111111 11111111 -> [255, 255, 255, 255]
        addr = []
        for octet in range(4):
            addr += [255 & self.address >> (8 * (3 - octet))]
        return iter(map(int, addr))

    def __getitem__(self, index):
        """Ipv4.__getitem__(index) <=> Ipv4[index] -> return int
        Fetches a the digit specified according to octet.
        Ipv4('192.168.0.1')[1] -> 168"""
        return tuple(self)[index]

    def __add__(self, other):
        """Ipv4.__add__(b) <=> Ipv4 + b -> return Ipv4"""
        return Ipv4(self.address + other)

    def __sub__(self, other):
        """Ipv4.__sub__(b) <=> Ipv4 - b -> return Ipv4"""
        return Ipv4(self.address - other)

    def __and__(self, other):
        """Ipv4.__and__(b) <=> Ipv4 & b -> return Ipv4"""
        return Ipv4(self.address & other)

    def __rand__(self, other):
        """Ipv4.__rand__(b) <=> b & Ipv4 -> return Ipv4"""
        return self & other

    def __or__(self, other):
        """Ipv4.__or__(b) <=> Ipv4 | b -> return Ipv4"""
        return Ipv4(self.address | other)

    def __ror__(self, other):
        """Ipv4.__ror__(b) <=> b | Ipv4 -> return Ipv4"""
        return self | other

    def __xor__(self, other):
        """Ipv4.__xor__(b) <=> Ipv4 ^ b -> return Ipv4"""
        return Ipv4(self.address ^ other)

    def __rxor__(self, other):
        """Ipv4.__xor__(b) <=> b ^ Ipv4 -> return Ipv4"""
        return self ^ other

    def __invert__(self):
        """Ipv4.__invert__() <=> ~Ipv4 -> return Ipv4"""
        return Ipv4(self ^ (2 ** 32 - 1))

__all__ = ['Ipv4']
