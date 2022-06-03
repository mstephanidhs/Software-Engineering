class Patient:
    def __init__(self, ID, ssn, firstName, lastName, phone, admitionDate, sex, dateOfBirth,
                 email, history, insurance, vitals, symptoms, address, maritalStatus, carePlan):
        self.patientID = ID
        self.ssn = ssn
        self.firstName = firstName
        self.lastName = lastName
        self.phone = phone
        self.admitionDate = admitionDate
        self.sex = sex
        self.dateOfBirth = dateOfBirth
        self.email = email
        self.history = history
        self.insurance = insurance
        self.vitals = vitals
        self.symptoms = symptoms
        self.address = address
        self.maritalStatus = maritalStatus
        self.carePlan = carePlan
        self.careTeam = []
        self.isActive = True
        self.examinationList = []

    def getPatientInfo(self):
        pass

    def getClinicalData(self):
        pass

    @staticmethod
    def checkEmail():
        pass

    def updatePatientStatus(self):
        pass

    def getCareTeam(self):
        pass

    @staticmethod
    def checkPhone():
        pass

    @staticmethod
    def checkSSN():
        pass

    def getMail(self):
        pass

    def updateCareTeam(self):
        pass
