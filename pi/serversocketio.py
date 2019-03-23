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
from flask import Flask
from flask_socketio import SocketIO, emit
# End third party imports.

# Start project imports.
# End project imports.


FLASK_OBJ = Flask(__name__)
SOCKET_IO_OBJ = SocketIO(FLASK_OBJ)
JSON_OBJ = dict()


@SOCKET_IO_OBJ.on('deposit', namespace='/bobby')
def deposit(receiveJsonObj):
    """
    """
    print('deposit')
    print(receiveJsonObj)
    global JSON_OBJ
    JSON_OBJ = receiveJsonObj
    emit('withdraw', JSON_OBJ, broadcast=True, namespace='/bobby')


if __name__ == '__main__':
    SOCKET_IO_OBJ.run(FLASK_OBJ)
