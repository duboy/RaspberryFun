#!/usr/bin/python

from __future__ import print_function
import sys
import binascii
import btle
import os

ble_conn = None

class MyDelegate(btle.DefaultDelegate):

    def __init__(self, conn):
        btle.DefaultDelegate.__init__(self)
        self.conn = conn

    def handleNotification(self, cHandle, data):
        data = binascii.b2a_hex(data)
        print("Notification:", str(cHandle), " data ", data)

    def handleDiscovery(self, dev, isNewDev, isNewData):
        if isNewDev:
            pass
        elif isNewData:
            print("\nDiscovery:", "MAC:", dev.addr, " Rssi ", str(dev.rssi))


def ble_connect(devAddr):
    global ble_conn
    if not devAddr is None and ble_conn is None:
        ble_conn = btle.Peripheral(devAddr, btle.ADDR_TYPE_PUBLIC)
        ble_conn.setDelegate(MyDelegate(ble_conn))
        print("connected")

def ble_disconnect():
    global ble_conn
    ble_conn = None
    print("disconnected")


if __name__ == '__main__':

    ble_mac == "66:55:44:33:22:11"

    # scan 
    scanner = btle.Scanner().withDelegate(MyDelegate(None))
    timeout = 10.0
    devices = scanner.scan(timeout)
    for dev in devices:
        if dev.addr == ble_mac:
            print("\nDiscovery:", "MAC:", dev.addr, " Rssi ", str(dev.rssi))
            for (adtype, desc, value) in dev.getScanData():
                print ("  %s(0x%x) = %s" % (desc, int(adtype), value))
            break

    # connect  
    ble_connect(ble_mac)
    # write , set listen
    snd_content_str = """\x01\x00"""
    ble_conn.writeCharacteristic(handle, snd_content_str)

    # wait notification  
    ble_conn.waitForNotifications(2.0)

    # disconnect 
    ble_disconnect()