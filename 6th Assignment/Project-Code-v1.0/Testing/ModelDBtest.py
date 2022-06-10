import sqlite3
import unittest
from Model.ModelDB import ModelDB
import PyQt5.QtWidgets as qtw

app = qtw.QApplication([])


class ModelDBTest(unittest.TestCase):

    def setUp(self):
        self.db = ModelDB('/home/dimitris/PycharmProjects/MedicWorld/Model/Medicine.sqlite3')

    def test_selectData(self):
        self.assertFalse(self.db.selectData("SELECT target from Medicine"))
        self.assertFalse(self.db.selectData("select fish from Medicine"))
        self.assertIsInstance(self.db.selectData("select name from Medicine"), list)
        self.assertIsInstance(self.db.selectData("select category from Medicine"), list)
        self.assertTrue(len(self.db.selectData("select name from Medicine")) > 0)

    def test_storeDate(self):
        self.assertFalse(self.db.storeData("Store values into INSERT INTO Medicine(name, category, quantity, minimum,\
            mediocre, low) VALUES (Antibiotics, Ponstan,100,100,1000,100);"))
        self.assertTrue(self.db.storeData(f"INSERT INTO Medicine(name, category, quantity, minimum,\
            mediocre, low) VALUES {'Ponstan', 'Antibiotics', 100, 100, 1000, 100};"))


if __name__ == '__main__':
    unittest.main()
