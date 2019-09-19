from unittest import *
from modAbs import *

class TestAbsValue(TestCase):
    def testPos(self):
        self.assertEqual(absValue(10),10)
    def testNeg(self):
        self.assertEqual(absValue(-10),10)

    def testZero(self):
        self.assertEqual(absValue(0),0)
#main
#main()
suite = TestLoader().loadTestsFromTestCase(TestAbsValue)
TextTestRunner(verbosity =2).run(suite)
