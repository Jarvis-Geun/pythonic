""" examples of unittest: assert """
# Reference: https://labs.brandi.co.kr/2018/06/07/kwakjs.html


from ex1_unittest import LibCalc
import unittest


class TddTest(unittest.TestCase):
    def testAdd(self):
        result = LibCalc.add(10, 20)
        self.assertEqual(result, 31)

    def testSubtract(self):
        result = LibCalc.subtract(20, 10)

        if result > 10:
            bool_val = True
        else:
            bool_val = False
        self.assertTrue(bool_val)

    def testDivision(self):
        self.assertRaises(ZeroDivisionError, LibCalc.division, 4, 1)

    def testMultiply(self):
        none_chk = True
        result = LibCalc.multiply(10, 9)
        if result > 100:
            none_chk = None
        self.assertIsNone(none_chk)


if __name__=="__main__":
    unittest.main()