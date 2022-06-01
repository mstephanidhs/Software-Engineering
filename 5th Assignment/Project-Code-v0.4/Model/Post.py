from datetime import datetime
from Model.HospitalStaffMember import  HospitalStaffMember

class Post:

    def __init__(self, ID, subject, content, timestamp, contributor, image):
        if not isinstance(int, ID):
            raise TypeError

        if not isinstance(str, subject):
            raise TypeError

        if not isinstance(str, content):
            raise TypeError

        if not isinstance(datetime, timestamp):
            raise TypeError

        if not isinstance(HospitalStaffMember, contributor):
            raise TypeError

        if not isinstance(bytearray, image):
            raise TypeError

        self.postID = ID
        self.subject = subject
        self.content = content
        self.timestamp = timestamp
        self.contributor = contributor
        self.rating = 0.0
        self.image = image

    def applyLanguageSelectorCheck(self):
        pass

    @staticmethod
    def checkRating():
        pass

    def deletePost(self):
        pass

    @staticmethod
    def checkImageSize():
        pass

    @staticmethod
    def checkTextSize():
        pass


