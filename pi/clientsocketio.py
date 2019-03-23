#!/usr/bin/env python
"""
[WHEN TO USE THIS FILE]
[INSTRUCTIONS FOR USING THIS FILE]

Project name: [MISSING]
Author: Micah Parks

This lives on the web at: [MISSING URL]
Target environment: python 3.7
"""

# Start standard library imports.
# End standard library imports.

# Start third party imports.
from socketio import Client
# End third party imports.

# Start project imports.
# End project imports.


def main() -> None:
    """
    The logic of the file.
    """
    clientObj = Client()
    clientObj.connect('http://127.0.0.1:5000/')
    clientObj.emit('deposit', {'foo': 'bar'}, namespace='/b2w')
    pass


if __name__ == '__main__':
    main()