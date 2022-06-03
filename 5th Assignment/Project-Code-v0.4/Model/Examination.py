class Examination:
    
    def __init__(self, ID , description , orderDatetime , completionDatetime ,results, patient , doctor , labTechnician ,lab):
        self.labTechnician = labTechnician
        self.doctor = doctor
        self.patient = patient
        self.lab = lab
        self.completionDatetime = completionDatetime
        self.orderDatetime = orderDatetime
        self.examID = ID
        self.description = description
        self.results = results
