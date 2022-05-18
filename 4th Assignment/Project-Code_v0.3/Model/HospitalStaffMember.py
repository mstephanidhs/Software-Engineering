import re
from datetime import datetime

EMAIL_PATTERN = re.compile(r'^[a-zA-Z0-9.!#$%&’*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$')


class HospitalStaffMember:

    def __init__(self, ID, firstName, lastName, position, username,
                 password, email, hireDate, phone, certification, schedule, department, iban):
        # if not isinstance(ID, int):
        #     raise ValueError(f"You have inserted type of {type(ID)} instead of <'int'>")
        self.__staffID = ID

        # if not isinstance(firstName, str):
        #     raise ValueError(f"You have inserted type of {type(firstName)} instead of <'str'>")
        self.firstName = firstName

        # if not isinstance(lastName, str):
        #     raise ValueError(f"You have inserted type of {type(lastName)} instead of <'str'>")
        self.lastName = lastName

        # if not isinstance(username, str):
        #     raise ValueError(f"You have inserted type of {type(username)} instead of <'str'>")
        self.__username = username

        # if not isinstance(password, str):
        #     raise ValueError(f"You have inserted type of {type(password)} instead of <'str'>")
        self.__password = password

        # if not isinstance(username, str):
        #     raise ValueError(f"You have inserted type of {type(username)} instead of <'str'>")
        # if not re.match(EMAIL_PATTERN, email):
        #     raise Exception("Not a valid email")
        self.__email = email

        # if not isinstance(hireDate, datetime):
        #     raise Exception("HireDate should be of type datetime")
        self.hireDate = hireDate

        # if not isinstance(phone, str):
        #     raise ValueError(f"You have inserted type of {type(phone)} instead of <'str'>")
        self.__phone = phone
        #
        # if not isinstance(position, str):
        #     raise ValueError(f"You have inserted type of {type(position)} instead of <'str'>")
        self.position = position

        # if not isinstance(certification, str):
        #     raise ValueError(f"You have inserted type of {type(certification)} instead of <'str'>")
        self.certification = certification

        self.schedule = schedule
        self.department = department
        self.__iban = iban


