# -*- coding: utf-8 -*-

from .ip import Ip

class Ipv6(Ip):

    @address.setter
    def address(self, address):
        pass


    def __init__(self, address):
        super(Ipv6, self).__init__()


    def __repr__(self):
        return "%s('%s')" %("Ipv6", str(self))


    def __str__(self):
        # should probably implement shorthand version, probably in a seperate
        # funcion
        return ":".join(tuple(self))


    def __tuple__(self):
        pass


    def __index__(self, index):
        return tuple(self)[index]


    def __add__(self, other):
        return self.address + other


    def __sub__(self, other):
        return self.address - other


    def __and__(self, other):
        return self.address & other


    def __or__(self, other):
        return self.address | other


    def __xor__(self):
        return self.address ^ other

__all__ = ['Ipv6']