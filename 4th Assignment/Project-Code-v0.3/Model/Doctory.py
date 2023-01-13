from HospitalStaffMember import HospitalStaffMember


class Doctor(HospitalStaffMember):

    def __init__(self, ID, firstName, lastName, position, username,
                 password, email, hireDate, phone, certification, schedule, department, specialization, rank, iban):
        super().__init__(ID, firstName, lastName, position, username, password, email,
                         hireDate, phone, certification, schedule, department, iban)
        self.rank = rank
        self.specialization = specialization
