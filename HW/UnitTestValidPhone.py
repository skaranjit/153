import unittest
from modValidatePhone import *

from unittest import *
class TestValidPhone(unittest.TestCase):
    def testFirstDigit(self):
        self.assertEqual(isValidPhone('0'),False)
        self.assertEqual(isValidPhone('123-458-1234'),True)
        self.assertEqual(isValidPhone('(123)458-1234'),True)
    def testLen(self):
        self.assertEqual(isValidPhone('111-124-1234'),True)
        self.assertEqual(isValidPhone('XXXxxxxxxxxxxxxx'),False)
        self.assertEqual(isValidPhone('123456789'),False)
    def testHypens(self):
        self.assertEqual(isValidPhone('123-456-7890'),True)
        self.assertEqual(isValidPhone('(123)458-1234'),True)
        self.assertEqual(isValidPhone('1231-123-111'),False)
        self.assertEqual(isValidPhone('123)55-458-1234'),False)
    def testDigitPlace(self):
        self.assertEqual(isValidPhone('123-125-1234'),True)
        self.assertEqual(isValidPhone('(123)125-1234'),True)
        self.assertEqual(isValidPhone('1a3-125-1234'),False)
        self.assertEqual(isValidPhone('AAASDQLLLSKDPQPSLD'),False)
        self.assertEqual(isValidPhone('(aa3)125-1234'),False)




if __name__== '__main__':
    unittest.main
suite = TestLoader().loadTestsFromTestCase(TestValidPhone)
TextTestRunner(verbosity =2).run(suite)

