import re
from datetime import datetime

EMAIL_PATTERN = re.compile(r'^[a-zA-Z0-9.!#$%&’*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$')


class HospitalStaffMember:

    def __init__(self, ID, firstName, lastName, position, username,
                 password, email, hireDate, phone, certification, schedule, department):
        if not isinstance(ID, int):
            raise ValueError(f"You have inserted type of {type(ID)} instead of <'int'>")
        self.__staffID = ID

        if not isinstance(firstName, str):
            raise ValueError(f"You have inserted type of {type(firstName)} instead of <'str'>")
        self.firstName = firstName

        if not isinstance(lastName, str):
            raise ValueError(f"You have inserted type of {type(lastName)} instead of <'str'>")
        self.lastName = lastName

        if not isinstance(username, str):
            raise ValueError(f"You have inserted type of {type(username)} instead of <'str'>")
        self.__username = username

        if not isinstance(password, str):
            raise ValueError(f"You have inserted type of {type(password)} instead of <'str'>")
        self.__password = password

        if not isinstance(username, str):
            raise ValueError(f"You have inserted type of {type(username)} instead of <'str'>")
        if not re.match(EMAIL_PATTERN, email):
            raise Exception("Not a valid email")
        self.__email = email

        if not isinstance(hireDate, datetime):
            raise Exception("HireDate should be of type datetime")
        self.hireDate = hireDate

        if not isinstance(phone, str):
            raise ValueError(f"You have inserted type of {type(phone)} instead of <'str'>")
        self.__phone = phone

        if not isinstance(position, str):
            raise ValueError(f"You have inserted type of {type(position)} instead of <'str'>")
        self.position = position

        if not isinstance(certification, str):
            raise ValueError(f"You have inserted type of {type(certification)} instead of <'str'>")
        self.certification = certification

        self.schedule = schedule
        self.department = department

    @property
    def staffID(self):
        return self.__staffID

    # @property
    # def firstName(self):
    #     return self.firstName

    # @firstName.setter
    # def firstName(self, value):
    #     self._firstName = value

    @property
    def lastName(self):
        return self.lastName

    @lastName.setter
    def lastName(self, value):
        self._lastName = value

    @property
    def position(self):
        return self.position

    @position.setter
    def position(self, value):
        self._position = value

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, newUserName):
        self.__username = newUserName

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, newPassword):
        self.__password = newPassword

    @property
    def hireDate(self):
        return self.hireDate

    @hireDate.setter
    def hireDate(self, value):
        self._hireDate = value

    @property
    def phone(self):
        return self.__phone

    @phone.setter
    def phone(self, value):
        self.__phone = value

    @property
    def certification(self):
        return self.certification

    @certification.setter
    def certification(self, value):
        self._certification = value

    @property
    def schedule(self):
        return self.schedule

    @schedule.setter
    def schedule(self, value):
        self._schedule = value

    @property
    def department(self):
        return self.department

    @department.setter
    def department(self, value):
        self._department = value



