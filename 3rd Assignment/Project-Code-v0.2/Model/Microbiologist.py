from HospitalStaffMember import HospitalStaffMember


class Microbiologist(HospitalStaffMember):

    def __init__(self, ID, firstName, lastName, position, username,
                 password, email, hireDate, phone, certification, schedule, department):
        super().__init__(ID, firstName, lastName, position, username, password, email,
                         hireDate, phone, certification, schedule, department)

