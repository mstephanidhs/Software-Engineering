
class Message:

    def __init__(self, ID, content, timestamp, status, senderID, receiverID):
        self.messageID = ID
        self.content = content
        self.timestamp = timestamp
        self.status = status
        self.senderID = senderID
        self.receiverID = receiverID
