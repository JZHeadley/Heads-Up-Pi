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
from bluetooth import PORT_ANY, RFCOMM, SERIAL_PORT_CLASS, SERIAL_PORT_PROFILE, BluetoothSocket, advertise_service
from socketio import Client
# End third party imports.

# Start project imports.
# End project imports.


CLIENT_OBJ = Client()


def main() -> None:
    """
    The logic of the file.
    """
    CLIENT_OBJ.connect('http://127.0.0.1:5000/')
    CLIENT_OBJ.emit('deposit', {'foo': 'bar'}, namespace='/bobby')
    CLIENT_OBJ.emit('deposit', {'332341': '36dfdsaf'}, namespace='/bobby')


if __name__ == '__main__':
    main()
