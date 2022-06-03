from HospitalStaffMember import HospitalStaffMember


class Doctor(HospitalStaffMember):

    def __init__(self, ID, firstName, lastName, position, username,
                 password, email, hireDate, phone, ssn, tin, iban, certification, schedule, department, status, rank,
                 specialization):
        super().__init__(ID, firstName, lastName, position, username,
                         password, email, hireDate, phone, ssn, tin, iban, certification, schedule, department, status)
        self.rank = rank
        self.specialization = specialization

    def getAvailability(self):
        pass

    def getPhone(self):
        pass

    def getMail(self):
        pass

    def getPassword(self):
        pass

    def getUsername(self):
        pass
