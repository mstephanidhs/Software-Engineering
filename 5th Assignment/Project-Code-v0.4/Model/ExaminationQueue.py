class ExaminationQueue():

    def __init__(self,doctor, patient,timestamp):
        self.__doctor = doctor
        self.__patient = patient
        self.timestamp = timestamp
        self.examination = []
