class PatientHistory():

    def __init__(self, ID, pastMedicalProblems, pastHospitalizations, pastMedication, familyRecords):
        self.historyID = ID
        self.pastMedicalProblems = pastMedicalProblems
        self.pastHospitalizations = pastHospitalizations
        self.pastMedication = pastMedication
        self.familyRecords = familyRecords
