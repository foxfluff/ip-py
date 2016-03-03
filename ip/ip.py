class Ip(object):

    @property
    def address(self):
        """Ip.address -> return address"""
        return self._address

    @address.setter
    def address(self, address):
        """Ip.address = address
        Assigns address"""
        # no definied structure for super, so just going to take an int and
        # store it
        if not isinstance(address, int) and not isinstance(address, long):
            raise TypeError
        self._address = address

    def __init__(self, address):
        """Ip(address) -> return Ip"""
        self.address = address

    def __repr__(self):
        """Ip.__repr__() <=> repr(Ip)"""
        return "%s(%s)" % ('Ip', self.address)

    def __add__(self, other):
        """Ip.__add__(b) <=> Ip + b -> return Ip"""
        return Ip(self.address + other)

    def __sub__(self, other):
        """Ip.__sub__(b) <=> Ip - b -> return Ip"""
        return Ip(self.address - other)

    def __and__(self, other):
        """Ip.__and__(b) <=> Ip & b -> return Ip"""
        return Ip(self.address & other)

    def __or__(self, other):
        """Ip.__or__(b) <=> Ip | b -> return Ip"""
        return Ip(self.address | other)

    def __xor__(self, other):
        """Ip.__xor__(b) <=> Ip ^ b -> return Ip"""
        return Ip(self.address ^ other)

    def __eq__(self, other):
        """Ip.__eq__(b) <=> Ip == b"""
        return self.address == other

    def __ne__(self, other):
        """Ip.__ne__(b) <=> Ip != b"""
        return self.address != other

    def __gt__(self, other):
        """Ip.__gt__(b) <=> Ip > b"""
        return self.address > other

    def __ge__(self, other):
        """Ip.__ge__(b) <=> Ip >= b"""
        return self.address >= other

    def __lt__(self, other):
        """Ip.__lt__(b) <=> Ip < b"""
        return self.address < other

    def __le__(self, other):
        """Ip.__le__(b) <=> Ip <= b"""
        return self.address <= other
