#!/usr/bin/env python3

import pytest
import os
import socket

ip = '192.168.100.100'
port = 9004
soc = None
buffsize = 20
timeout = 1

class Test_SR2000(object):
        
    def test_ping(self):

        response = os.system("ping -c 1 " + ip)
        assert response == 0, "error ip, please check barcode scanner ip"

    def test_connect(self):
        print('Opening socket on {0}:{1}'.format(ip, port))
        
        soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        soc.settimeout(timeout)
        soc.connect((ip, port))

        if soc != None:
            soc.close()

        print('Keyence Reader socket successfully opened!')

        assert soc != None, "socket error!"