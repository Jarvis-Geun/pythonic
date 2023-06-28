""" example of unittest """

# Reference: https://labs.brandi.co.kr/2018/06/07/kwakjs.html

import unittest


class LibCalc:
    def add(a, b):
        return a + b
    
    def subtract(a, b):
        return a - b
    
    def division(a, b):
        return a / b
    
    def multiply(a, b):
        return a * b
    

class TddTest(unittest.TestCase):
    def testAdd(self):
        result = LibCalc.add(10, 20)
        if result == 30:
            print("testAdd OK")

    def testSubtract(self):
        result = LibCalc.subtract(10, 20)
        if result > 0:
            bool_val = True
        else:
            bool_val = False

        if bool_val == False:
            print("testSubtract Error")

    def testDivsion(self):
        try:
            LibCalc.division(4, 0)
        except Exception as e:
            print(e)
    
    def testMultiply(self):
        result = LibCalc.multiply(10, 9)

        if result < 100:
            print("testMultiply Error")


if __name__=="__main__":
    unittest.main()