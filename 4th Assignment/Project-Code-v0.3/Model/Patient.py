class Patient:
    def __init__(self, ID, ssn, firstName, lastName, phone, admittionDate, sex, dateOfBirth,
                 email, history, insurance, vitals, symptoms, address, maritalStatus, carePlan):

        self.patientID = ID
        self.ssn = ssn
        self.firstName = firstName
        self.lastName = lastName
        self.phone = phone
        self.admittionDate = admittionDate
        self.sex = sex
        self.dateOfBirth = dateOfBirth
        self.email = email
        self.history = history
        self.insurance = insurance
        self.vitals = vitals
        self.symptoms = symptoms
        self.address = address
        self.maritalStatus = maritalStatus
        self.carePlan =carePlan