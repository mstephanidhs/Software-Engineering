import re
import sqlite3


class Drug:
    def __init__(self, name, category, quantity, minn, med, low):
        if not isinstance(name, str):
            raise TypeError(f" 'name' should be <class 'str'>, you have given {type(name)} ")
        self.name = name
        if not isinstance(low, int):
            raise TypeError(f" 'low' should be <class 'str'>, you have given {type(low)} ")
        self.low = low
        if not isinstance(med, int):
            raise TypeError(f" 'med' should be <class 'str'>, you have given {type(med)} ")
        self.med = med
        if not isinstance(minn, int):
            raise TypeError(f" 'minn' should be <class 'str'>, you have given {type(minn)} ")
        self.min = minn
        if not isinstance(category, str):
            raise TypeError(f" 'category' should be <class 'str'>, you have given {type(category)} ")
        self.category = category
        self.quantity = quantity

    @staticmethod
    def drugExists(drugList, name):
        for drug in drugList:
            if drug == name:
                return True
        return False

    @staticmethod
    def quantitiesCheck(quantities):
        regexNumber = re.compile(r'[0-9]+')
        try:
            if regexNumber.match(quantities):
                return True
            return False
        except TypeError:
            return False

    @staticmethod
    def checkCategory(drugCategory,connector):
        drugCategories = connector.selectData("select distinct category from Medicine")
        drugCategories = [x[0] for x in drugCategories]
        if drugCategory not in drugCategories:
            return True
        return False


    def show(self):
        return self.category, self.name, self.quantity, self.min, self.med, self.low

    def store(self, connector):
        try:
            connector.storeData(
                f"INSERT INTO Medicine(name, category, quantity, minimum, mediocre, low) VALUES {self.show()};")
            return True
        except sqlite3.Error as e:
            raise e
