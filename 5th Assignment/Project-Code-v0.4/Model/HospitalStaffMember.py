import re
from datetime import datetime

EMAIL_PATTERN = re.compile(r'^[a-zA-Z0-9.!#$%&’*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$')


class HospitalStaffMember:

    def __init__(self, ID, firstName, lastName, position, username,
                 password, email, hireDate, phone, ssn,tin,iban, certification, schedule, department,status ):
        self.__staffID = ID
        self.__firstName = firstName
        self.__lastName = lastName
        self.__username = username
        self.__password = password
        self.__email = email
        self.__hireDate = hireDate
        self.__phone = phone
        self.__position = position
        self.__certification = certification
        self.__schedule = schedule
        self.__department = department
        self.__iban = iban
        self.__ssn = ssn
        self.__tin = tin
        self.__activeEmployee = True
        self.__status = status
        self.isActive = True
        self.__badge = ""
        self.__ratings = 0.0

    def getAvailability(self):
        pass

    def updateAvailabilityStatus(self):
        pass

    def updateActivityStatus(self):
        pass

    def getTotalRating(self):
        pass

    def updateBadge(self):
        pass

    def updateTotalRatings(self):
        pass

    def isBadgeWorthy(self):
        pass

    @staticmethod
    def checkUsername():
        pass

    @staticmethod
    def checkTIN():
        pass

    @staticmethod
    def checkSSN():
        pass

    @staticmethod
    def checkIBAN():
        pass


