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
from json import loads
# End standard library imports.

# Start third party imports.
from bluetooth import PORT_ANY, RFCOMM, SERIAL_PORT_CLASS, SERIAL_PORT_PROFILE, BluetoothSocket, advertise_service
from socketio import Client
# End third party imports.

# Start project imports.
# End project imports.


CLIENT_OBJ = Client()
BLUETOOTH_SOCKET_OBJ = BluetoothSocket(RFCOMM)
BLUETOOTH_SOCKET_OBJ.bind((str(), PORT_ANY))
BLUETOOTH_SOCKET_OBJ.listen(1)
PORT_INT = BLUETOOTH_SOCKET_OBJ.getsockname()[1]
UUID_STR = '94f39d29-7d6d-437d-973b-fba39e49d4ee'


def get_json_from_socket(socketObj) -> dict:
    """"
    """
    receiveBytes = socketObj.recv(1024)
    if len(receiveBytes) == 0:
        return None
    return loads(receiveBytes.decode('utf-8'))


def main() -> None:
    """
    The logic of the file.
    """
    CLIENT_OBJ.connect('http://127.0.0.1:5000/')
    advertise_service(BLUETOOTH_SOCKET_OBJ, 'SampleServer', service_id=UUID_STR,
                      service_classes=[UUID_STR, SERIAL_PORT_CLASS],
                      profiles=[SERIAL_PORT_PROFILE])
    try:
        while True:
            print('Waiting for connection on RFCOMM channel "{}"...'.format(PORT_INT))
            socketObj, infoTuple = BLUETOOTH_SOCKET_OBJ.accept()
            print('Accepted connection from "{}".'.format(infoTuple))
            try:
                print('Entering main data loop.')
                while True:
                    emitDict = get_json_from_socket(socketObj=socketObj)
                    if emitDict is not None:
                        print('Sending data: "{}".'.format(emitDict))
                        CLIENT_OBJ.emit('deposit', emitDict)
            except IOError as exceptionStr:
                print('Exception occured: "{}"'.format(exceptionStr))
                pass
            socketObj.close()
            print('Disconnected.')
    except Exception as exceptionStr:
        print('Unhanded exception. Retrying...')
        try:
            BLUETOOTH_SOCKET_OBJ.close()
        except Exception as exceptionStr:
            pass
    print('Done')


if __name__ == '__main__':
    main()
