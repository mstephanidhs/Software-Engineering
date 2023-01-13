class OperatingRoom:

    def __init__(self, ID, name, isOccuppied, procedure, patient, department,l):
        self.roomID = ID
        self.name = name
        self.isOccupied = isOccuppied
        self.occupationReason = procedure
        self.patient = patient
        self.department = department
        self.assignedPersonnel = []

        