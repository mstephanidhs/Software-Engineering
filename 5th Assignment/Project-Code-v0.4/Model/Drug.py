class Drug:

    def __init__(self, ID, name, capacity, expirationDate, description, sideEffects, category):
        self.drugID = ID
        self.name = name
        self.capacity = capacity
        self.expirationDate = expirationDate
        self.description = description
        self.sideEffects = sideEffects
        self.category = category

    @staticmethod
    def drugExists():
        pass
