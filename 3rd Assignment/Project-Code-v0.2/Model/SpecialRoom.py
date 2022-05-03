class SpecialRoom:

    def __init__(self, ID, name, isOccuppied, occupationReason, patient, department):
        self.roomID = ID
        self.name = name
        self.isOccupied = isOccuppied
        self.occupationReason = occupationReason
        self.patient = patient
        self.department = department
        self.assignedPersonnel = []
        