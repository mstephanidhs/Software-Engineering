from HospitalStaffMember import HospitalStaffMember


class Nurse(HospitalStaffMember):

    def __init__(self, ID, firstName, lastName, position, username,
                 password, email, hireDate, phone, certification, schedule, department, specialization):
        super().__init__(ID, firstName, lastName, position, username, password, email,
                         hireDate, phone, certification, schedule, department)
        self.specialization = specialization
