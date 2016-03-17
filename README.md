# ip-py

## Synopsis

A module for Python 2.x that creates classes to handle data types of IPv4 and IPv6 addresses, providing arithmetic functions to easy usage of the given addressing scheme.

## Code Example

```
>>> Ipv4_obj = ip.Ipv4('192.168.0.1')
>>> Ipv4_obj + 500
Ipv4('192.168.1.245')
>>> Ipv4_obj - 500
Ipv4('192.167.254.13')
>>> list(Ipv4)
[192, 168, 0, 1]
...
```

## Motivation

The original purpose of this project was to make handling IPv4 addresses considerably easier, with the intention of writing a future networking module that would use this.
Ipv6 was added shortly after for the prospects of also writing an Ipv6 networking module in the future.

## Installation

```
import ip
```

Currently no setup script, planned on being implemented for v1.0

## API Reference

You can use the builtin help() function to provide documentation for certain functions.

## Tests

A single test script is included with the module, just run the following:

```
python test.py
```

## License

MIT License applies (see LICENSE)
