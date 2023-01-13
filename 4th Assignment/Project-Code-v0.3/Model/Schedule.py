class Schedule:
    def __init__(self, startTime, endTime, shiftType):
        self.startTime = startTime
        self.endTime = endTime
        self.shiftType = shiftType
        self.tasks = []