#!/usr/bin/env python
import socket
import rospy
import time
from std_srvs.srv import Trigger, TriggerResponse

class SR2000:
    def __init__(self):
        self._ip = '192.168.100.100'
        self._port = 9004
        self._socket = None
        self._buffsize = 20
        self._timeout = 1

        self.connect()

        rospy.Service("/read_barcode", Trigger, self.read)
        rospy.Service("/tune_focus", Trigger, self.tune_focus)

    def connect(self):
        rospy.loginfo('Opening socket on {0}:{1}'.format(self._ip, self._port))
        if self._socket != None:
            self._socket.close()

        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._socket.settimeout(self._timeout)
        self._socket.connect((self._ip, self._port))
        rospy.loginfo('Keyence Reader Socket successfully opened!')

    def read(self, req):
        self._socket.send("LON\r")
        res = TriggerResponse()
        res.success = True
        try:
            res.message = self._socket.recv(self._buffsize).split('\r')[0]
        except IOError:
            self._socket.send("LOFF\r")
            res.message = self._socket.recv(self._buffsize).split('\r')[0]

        return res

    def tune_focus(self, req):
        self._socket.send("FTUNE\r")
        res = TriggerResponse()
        res.success = True
        res.message = self._socket.recv(50).split('\r')[1][13:]

        return res

if __name__ == '__main__':
    rospy.init_node('barcode_reader_node')
    node = SR2000()
    rospy.spin()