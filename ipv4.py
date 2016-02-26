# -*- coding: utf-8 -*-

from .ip import Ip

class Ipv4(Ip):

    @address.setter
    def address(self, address):
        pass


    def __init__(self, address):
        super(Ipv4, self).__init__()


    def __repr__(self):
        return "%s('%s')" %("Ipv4", str(self))


    def __str__(self):
        return ".".join(tuple(self))


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


__all__ = ['Ipv4']