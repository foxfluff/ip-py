class Ip(object):

    @property
    def address(self):
        return self._address


    @address.setter
    def address(self, address):
        # no definied structure for super, so just going to take an int and
        # store it
        if not isinstance(address, int) and not isinstance(address, long):
            raise TypeError
        self._address = address


    def __init__(self, address):
        self.address = address


    def __repr__(self):
        return "%s(%s)" %('Ip', self.address)


    def __add__(self, other):
        return Ip(self.address + other)


    def __sub__(self, other):
        return Ip(self.address - other)


    def __and__(self, other):
        return Ip(self.address & other)


    def __or__(self, other):
        return Ip(self.address | other)


    def __xor__(self, other):
        return Ip(self.address ^ other)


    def __eq__(self, other):
        return self.address == other


    def __ne__(self, other):
        return self.address != other


    def __gt__(self, other):
        return self.address > other


    def __ge__(self, other):
        return self.address >= other


    def __lt__(self, other):
        return self.address < other


    def __le__(self, other):
        return self.address <= other
