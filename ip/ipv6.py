from ip import Ip

class Ipv6(Ip):

    _delimiter = ':'
    # technically speaking there is no global broadcast, need to find a better
    # term for this.
    GLOBAL_BROADCAST = "ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff"

    @property
    def address(self):
        return super(Ipv6, self).address

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
                print _addr, location
                raise ValueError(
                    'Expected at most one "%s", IPv6 does not support more' %
                    (self._delimiter * 2))
            return list_addr(_addr)

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
        super(Ipv6, self).__init__(address)


    def __repr__(self):
        return "%s('%s')" % ("Ipv6", str(self))


    def __str__(self):
        # should probably implement shorthand version, probably in a seperate
        # funcion
        return self._delimiter.join(
            map(self._hex_digit, tuple(self))
            )


    def __iter__(self):
        # GLORIOUS COPY PASTE/MINOR TWEAKS
        addr = []
        for digit in range(8):
            addr += [65535 & self.address >> (16 * (7 - digit))]
        return iter(map(self._dec_digit, addr))


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
        return Ipv6(self ^ Ipv6(self.GLOBAL_BROADCAST))

__all__ = ['Ipv6']
