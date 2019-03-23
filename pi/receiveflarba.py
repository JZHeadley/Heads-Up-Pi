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
# End third party imports.

# Start project imports.
from flask import Flask, render_template
from flask_socketio import SocketIO, emit
# End project imports.


FLASK_OBJ = Flask(__name__)
SOCKET_IO_OBJ = SocketIO(FLASK_OBJ)


@SOCKET_IO_OBJ.on('flarba', namespace='/narba')
def get_flarba(receiveJson):
    """
    """
    print('flarba received: {}'.format(receiveJson))


if __name__ == '__main__':
    SOCKET_IO_OBJ.run(FLASK_OBJ)
