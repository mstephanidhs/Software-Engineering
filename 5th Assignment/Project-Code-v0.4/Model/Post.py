from datetime import datetime
from Model.HospitalStaffMember import  HospitalStaffMember
import os
class Post:

    def __init__(self, ID, subject, content, timestamp, contributor, image):


        if len(content) > 280:
            raise Exception

        if os.path.getsize(image) > 60000000:
            raise Exception

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


