""" example of unittest: setUp(), tearDown() """
# Reference: https://labs.brandi.co.kr/2018/06/07/kwakjs.html

from ex1_unittest import LibCalc
import unittest


class TddTest(unittest.TestCase):
    aa = 0
    bb = 0
    result = 0

    def setUp(self) -> None:
        self.aa = 10
        self.bb = 20

    def testAdd(self):
        self.result = LibCalc.add(self.aa, self.bb)
        self.assertEqual(self.result, 31)

    def testSubtract(self):
        self.result = LibCalc.subtract(self.aa, self.bb)
        if self.result > 10:
            bool_val = True
        else:
            bool_val = False
        self.assertTrue(bool_val)

    def testDivsion(self):
        self.assertRaises(ZeroDivisionError, LibCalc.division, 4, 1)
    
    def testMultiply(self):
        none_chk = True
        self.result = LibCalc.multiply(10, 9)
        if self.result > 100:
            none_chk = None
        self.assertIsNone(none_chk)

    def tearDown(self) -> None:
        print("result: " + str(self.result))


if __name__=="__main__":
    unittest.main()