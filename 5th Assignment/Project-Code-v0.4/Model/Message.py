from datetime import datetime


class Message:

    def __init__(self, ID, content, timestamp, status, senderID, receiverID):

        if not isinstance(int, ID):
            raise TypeError

        if not isinstance(str, content):
            raise TypeError

        if not isinstance(datetime, timestamp):
            raise TypeError

        if not isinstance(bool, status):
            raise TypeError

        if not isinstance(int, receiverID):
            raise TypeError

        if not isinstance(int, senderID):
            raise TypeError

        self.messageID = ID
        self.content = content
        self.timestamp = timestamp
        self.status = status
        self.senderID = senderID
        self.receiverID = receiverID

    def sendMessage(self, receiver):
        pass

    def updateStatus(self, value):
        self.status = value

    def createAutomatedMessage(self):
        pass
