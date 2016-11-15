import unittest

def isEven(n):
    return n % 2 == 0

class IsEvenTests(unittest.TestCase):
    #each method is a test to be round
    def testTwo(self):
        self.failUnless(isEven(2))
    def testThree(self):
        self.failUnless(isEven(4))

# Think of Feature->Write Tests->Run & Fail->Code->Run & Pass->Refactor->Repeat

class TruthTest(unittest.TestCase):
    def test_asset_true(self):
        my_value = True
        self.assertTrue(my_value)
    def test_asset_false(self):
        my_value = False
        self.assertFalse(my_value)
if __name__ == '__main__':
    unittest.main()
