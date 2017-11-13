from bluepy.btle import Scanner, DefaultDelegate
class ScanDelegate(DefaultDelegate): 
    def __init__(self): 
        DefaultDelegate.__init__(self)
    def handleDiscovery(self, dev, isNewDev, isNewData): 
        if isNewDev: 
            print "Discovered device", dev.addr 
        elif isNewData: 
            print "Received new data from", dev.addr
scanner = Scanner().withDelegate(ScanDelegate()) 
devices = scanner.scan(1.0)
for dev in devices:
	print devices.addr;