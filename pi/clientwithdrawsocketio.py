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


CLIENT_OBJ = Client()


@CLIENT_OBJ.on('withdraw')
def message(jsonObj):
    """
    """
    print('got message')
    print(jsonObj)


def main() -> None:
    """
    The logic of the file.
    """
    CLIENT_OBJ.connect('http://127.0.0.1:5000/')
    # while True:

    CLIENT_OBJ.wait()


if __name__ == '__main__':
    main()
