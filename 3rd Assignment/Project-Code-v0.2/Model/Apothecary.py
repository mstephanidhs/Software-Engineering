
class Apothecary:

    def __init__(self, apothecaryID, drugCapacity, department):
        self.apothecaryID = apothecaryID
        self.drugCapacity = drugCapacity
        self.department = department
        self.assignedPharmacist = ''
        self.drugList = []

        