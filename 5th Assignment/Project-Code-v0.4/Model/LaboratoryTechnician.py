from HospitalStaffMember import HospitalStaffMember


class LaboratoryTechnician(HospitalStaffMember):

    def __init__(self, ID, firstName, lastName, position, username,
                 password, email, hireDate, phone, ssn, tin, iban, certification, schedule, department, status,
                 specialization):
        super().__init__(ID, firstName, lastName, position, username,
                         password, email, hireDate, phone, ssn, tin, iban, certification, schedule, department, status)
        self.specialization = specialization
        self.assignedQueue = None


    def getAvailability(self):
        pass
