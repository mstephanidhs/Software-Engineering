class OperatingRoom:

    def __init__(self, ID, name, isOccupied, procedure, patient, assignedPersonell, department):
        self.roomID = ID
        self.name = name
        self.isOccupied = isOccupied
        self.procedure = procedure
        self.patient = patient
        self.assignedPersonnel = assignedPersonell
        self.department = department
        self.equipmentList = []

    def getAvailability(self):
        pass

    def getEquipment(self):
        pass

    def getDepartment(self):
        pass
