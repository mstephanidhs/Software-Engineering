from HospitalStaffMember import HospitalStaffMember
from datetime import datetime

class Microbiologist(HospitalStaffMember):

    def __init__(self, ID, firstName, lastName, position, username,
                 password, email, hireDate, phone, certification, schedule, department, iban):
        super().__init__(ID, firstName, lastName, position, username, password, email,
                         hireDate, phone, certification, schedule, department, iban)


p1 = Microbiologist(12,"Dimitris","Verginis","asdf","asdfsfd","asd;flk","d.ve@gmai.com",datetime(1231,1,1),"123412341243","asdfasdf","asdfsadf","asdfsdf")
print(isinstance(p1))