
class Event:

    def __init__(self, type, name, startDate, endDate, participants, description, location):
        self.eventType = type
        self.name = name
        self.startDate = startDate
        self.endDate = endDate
        self.participants = participants
        self.description = description
        self.location = location

    @staticmethod
    def checkName():
        pass

    @staticmethod
    def checkDate():
        pass

    @staticmethod
    def checkURL():
        pass

    @staticmethod
    def checkDescription():
        pass
