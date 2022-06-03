from datetime import datetime

class Notification:

    def __init__(self, ID, message, timestamp, receiver):

        self.notificationID = ID
        self.message = message
        self.timestamp = timestamp
        self.receiver = receiver

    def sendNotification(self):
        pass