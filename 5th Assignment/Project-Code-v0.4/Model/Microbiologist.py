from HospitalStaffMember import HospitalStaffMember
from datetime import datetime


class Microbiologist(HospitalStaffMember):

    def __init__(self, ID, firstName, lastName, position, username,
                 password, email, hireDate, phone, ssn, tin, iban, certification, schedule, department, status):
        super().__init__(ID, firstName, lastName, position, username,
                         password, email, hireDate, phone, ssn, tin, iban, certification, schedule, department, status)


