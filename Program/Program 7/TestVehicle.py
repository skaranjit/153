import unittest
from modVehicle import *

from unittest import *
class TestValidVehicle(unittest.TestCase):
    def testFirstDigit(self):
        self.assertEqual(isValidSSN('0'),False)
        self.assertEqual(isValidSSN('123-45-1234'),True)
    def testLen(self):
        self.assertEqual(isValidSSN('111-12-1234'),True)
        self.assertEqual(isValidSSN('xxxxxxxxxxxxx'),False)
        self.assertEqual(isValidSSN('123456789'),False)
    def testHypens(self):
        self.assertEqual(isValidSSN('123-45-7890'),True)
        self.assertEqual(isValidSSN('1231-123-111'),False)
    def testDigitPlace(self):
        self.assertEqual(isValidSSN('123-12-1234'),True)
        self.assertEqual(isValidSSN('1212-1234-12'),False)



if __name__== '__main__':
    unittest.main
suite = TestLoader().loadTestsFromTestCase(TestValidSSN)
TextTestRunner(verbosity =2).run(suite)

