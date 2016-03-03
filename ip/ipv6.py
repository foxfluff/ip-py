from ip import Ip

class Ipv6(Ip):

    @property
    def address(self):
        """Ipv6.address -> return address"""
        return super(Ipv6, self).address

    @address.setter
    def address(self, address, delimiter = ":"):
        """Ipv6.address = address
        Assigns address"""
        def list_addr(addr):
            """list_addr(addr)
            Takes a list of digits representing an Ipv6 address and converts
            it to a single long"""
            if len(addr) != 8:
                raise ValueError('Expected 8 octet address, got %i in (%s)' %
                                 (len(addr), address))
            # converts a list into a single long
            _addr = 0
            #for octet in range(4):
                #_addr += addr[octet] * 2 ** (8 * (3 - octet))
            #return _addr
            #eww copy paste
            _addr = 0
            _digit = 0
            for digit in range(8):
                # assume hex if a string? base10 if an int? sure why not
                # convert to int for ease of use I suppose.
                if isinstance(addr[digit], str):
                    _digit = int(addr[digit], 16)
                elif (isinstance(addr[digit], int) or
                    isinstance(addr[digit], long)):

                    _digit = int(addr[digit])
                _addr += _digit << (16 * (7 - digit))

            return _addr

        def string_addr(addr):
            """string_addr(addr)
            Takes a string representing an Ipv6 address, and converts it to a
            single long"""
            _addr = addr.split(self._delimiter)
            if _addr[:2] == ['', ''] or _addr[-2:] == ['', '']:
                # special case when '::' is on the outer most digit, causes
                # .split to behave in a way we don't like
                _addr.remove('')
            if '' in _addr:
                location = _addr.index('')
                _addr.remove('')
                _addr = (
                    _addr[:location] +
                    ([0] * (8 - len(_addr))) +
                    _addr[location:])
            if '' in _addr:
                #indicates two '::', which is not possible in ipv6 addresses
                raise ValueError(
                    'Expected at most one "%s", IPv6 does not support more' %
                    (self._delimiter * 2))
            return list_addr(_addr)

        self._delimiter = delimiter
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
        return hex(digit)[2:].rjust(4, '0')

    def _dec_digit(self, digit):
        # this seems silly
        return int(digit)

    def __init__(self, address):
        """Ipv6(address) -> return Ipv6"""
        super(Ipv6, self).__init__(address)

    def __repr__(self):
        """Ipv6.__repr__() <=> repr(Ipv6)"""
        return "%s('%s')" % ("Ipv6", str(self))

    def __str__(self):
        """Ipv6.__str__() <=> str(Ipv6)
        NOTE: This returns the fully expanded address in all lowercase hex"""
        # should probably implement shorthand version, probably in a seperate
        # funcion
        return self._delimiter.join(
            map(self._hex_digit, tuple(self))
            )

    def __iter__(self):
        """Ipv6.__iter__() <=> iter(Ipv6)"""
        # GLORIOUS COPY PASTE/MINOR TWEAKS
        addr = []
        for digit in range(8):
            addr += [65535 & self.address >> (16 * (7 - digit))]
        return iter(map(self._dec_digit, addr))

    def __getitem__(self, index):
        """Ipv6.__getitem__(index) <=> Ipv6[index] -> return int
        Fetches a the digit specified according to 2 byte chunks.
        Ipv6('1234:5678:9abc:ef01:2345:6789:abcd')[1] -> 5678"""
        return tuple(self)[index]

    def __add__(self, other):
        """Ipv6.__add__(b) <=> Ipv6 + b -> return Ipv6"""
        return Ipv6(self.address + other)

    def __sub__(self, other):
        """Ipv6.__sub__(b) <=> Ipv6 - b -> return Ipv6"""
        return Ipv6(self.address - other)

    def __and__(self, other):
        """Ipv6.__and__(b) <=> Ipv6 & b -> return Ipv6"""
        return Ipv6(self.address & other)

    def __rand__(self, other):
        """Ipv6.__rand__(b) <=> b & Ipv6 -> return Ipv6"""
        return self & other

    def __or__(self, other):
        """Ipv6.__or__(b) <=> Ipv6 | b -> return Ipv6"""
        return Ipv6(self.address | other)

    def __ror__(self, other):
        """Ipv6.__ror__(b) <=> b | Ipv6 -> return Ipv6"""
        return self | other

    def __xor__(self, other):
        """Ipv6.__xor__(b) <=> Ipv6 ^ b -> return Ipv6"""
        return Ipv6(self.address ^ other)

    def __rxor__(self, other):
        """Ipv6.__xor__(b) <=> b ^ Ipv6 -> return Ipv6"""
        return self ^ other

    def __invert__(self):
        """Ipv6.__invert__() <=> ~Ipv6 -> return Ipv6"""
        return Ipv6(self ^ (2 ** 128 - 1))

__all__ = ['Ipv6']
