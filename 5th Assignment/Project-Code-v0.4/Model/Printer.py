class Printer:

    def __init__(self, ID, macAddress):

        self.printerID = ID
        self.macAddress = macAddress
        self.queue = []
        self.isAvailable = True


    def addToPrinterQueue(self):
        pass

    def printSuccessful(self):
        pass

    def removeFromQueue(self):
        pass
