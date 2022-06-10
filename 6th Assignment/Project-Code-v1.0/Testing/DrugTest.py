import sqlite3
import unittest
from Model.ModelDB import ModelDB
from Model.Drug import  Drug


class DrugTest(unittest.TestCase):

    def testInit(self):
        self.assertRaises(TypeError, Drug,"Ponstan", 123, 100,100,100, 100)
        drug = Drug("Ponstan", "Antibiotics", 100,100,100, 100)
        self.assertIsInstance(drug, Drug,"given object is not instance of Drug")
        self.assertRaises(TypeError, Drug, ['test','ponstan'], "Antiobitics", 100, 100, 100, 100)
        self.assertRaises(TypeError, Drug, ["Dulcolax"], "Antiobitics", 100, 100, 100, 100)
        self.assertRaises(TypeError, Drug, "Ponstan", "Antiobitics", 100, 100, 'test', 100)
        self.assertRaises(TypeError, Drug, "Ponstan", "Antiobitics", 100, '100', 100, 100)
        self.assertRaises(TypeError, Drug, "Ponstan", "Antiobitics", 100, 100, 100, '100')

    def testShow(self):
        drug = Drug("Ponstan", "Antibiotics", 100, 100, 100, 100)
        self.assertEqual(len(drug.show()), 6)

    def test_drugExists(self):
        drugList = ["Ponstan", "Dulcolax", "Paracetamol", "Depon"]
        self.assertTrue(Drug.drugExists(drugList,"Ponstan"))
        self.assertFalse(Drug.drugExists(drugList,"Ponsta"))
        self.assertFalse(Drug.drugExists(drugList,"Algofren"))
        self.assertTrue(Drug.drugExists(drugList,"Depon"))

    def test_quantitiesCheck(self):
        self.assertTrue(Drug.quantitiesCheck("123"))
        self.assertTrue(Drug.quantitiesCheck("100"))
        self.assertFalse(Drug.quantitiesCheck("asdf"))
        self.assertFalse(Drug.quantitiesCheck([123]))

    def test_store(self):
        db =ModelDB('/home/dimitris/PycharmProjects/MedicWorld/Model/Medicine.sqlite3')
        drug1 = Drug("Antibiotics", "Ponstan", 100, 100, 100, 100)
        drug2 = Drug("Antibiotics", "Ponstan", 500, 100, 100, 100)
        self.assertTrue(drug1.store(db))
        self.assertTrue(drug2.store(db))

if __name__ == '__main__':
    unittest.main()
