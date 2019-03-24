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


def process_json(jsonObj):
    """
    {
    lat: location.latitude,
    long: + location.longitude,
    speed: abs(speedVal),
    bearing: bearingVal
    }
    """
    bearingFloat = float(jsonObj['bearing'])
    if -22.5 <= bearingFloat <= 22.5:
        jsonObj['bearing'] = 'N'
    elif 22.5 < bearingFloat < 67.5:
        jsonObj['bearing'] = 'NE'
    elif 67.5 <= bearingFloat <= 112.5:
        jsonObj['bearing'] = 'E'
    elif 112.5 < bearingFloat < 157.5:
        jsonObj['bearing'] = 'SE'
    elif 157.5 <= bearingFloat <= 180 or -180 <= bearingFloat <= -157.5:
        jsonObj['bearing'] = 'S'
    elif -157.5 < bearingFloat < -122.5:
        jsonObj['bearing'] = 'SW'
    elif -122.5 <= bearingFloat <= -67.5:
        jsonObj['bearing'] = 'W'
    elif -67.5 < bearingFloat < -22.5:
        jsonObj['bearing'] = 'NW'
    if isinstance(jsonObj['bearing'], float):
        jsonObj['bearing'] = 'Micah or Zephyr is dum.'
    return jsonObj


@SOCKET_IO_OBJ.on('deposit')
def deposit(receiveJsonObj):
    """
    """
    print('deposit')
    print(receiveJsonObj)
    global JSON_OBJ
    JSON_OBJ = process_json(jsonObj=receiveJsonObj)
    emit('withdraw', JSON_OBJ, broadcast=True)


if __name__ == '__main__':
    SOCKET_IO_OBJ.run(FLASK_OBJ)
