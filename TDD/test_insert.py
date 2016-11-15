import unittest

from insert_value import insert_val_at

class InsertValueTest(unittest.TestCase):
    def setUp(self):
        self.test_list = [1,2,3]
        self.result = insert_val_at(2, self.test_list, 4)
        self.result2 = insert_val_at(6, self.test_list, 3)
    def testInsertAtIndexTwo(self):
        return self.assertEqual([1,2,3], self.result)
    def testReturnFalseForInvalidIndex(self):
        return self.assertEqual(False, self.result2)
if __name__ == "__main__":
    unittest.main()
