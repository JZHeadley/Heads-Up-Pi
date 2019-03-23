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
from socketio import Client
# End project imports.


if __name__ == '__main__':
    clientObj = Client()
    clientObj.connect('http://localhost:5000')
    # for a in range(1000):
    clientObj.emit('flarba', {'foo': 'bar'}, namespace='/narba')
