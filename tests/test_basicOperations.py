import unittest
from AdvancedCalculator.basicOperations import add, sub, mul, div


class TestMathOperation(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(10, 5), 15)
        self.assertEqual(add(-1, -2), -3)
        self.assertEqual(add(4, -5), -1)
        self.assertEqual(add(0, 0), 0)

    def test_sub(self):
        self.assertEqual(sub(10, 5), 5)
        self.assertEqual(sub(-1, -2), 1)
        self.assertEqual(sub(4, -5), 9)
        self.assertEqual(sub(-7, 3), -10)

    def test_mul(self):
        self.assertEqual(mul(2,2), 4)
        self.assertEqual(mul(-3, -4), 12)
        self.assertEqual(mul(-2, 5), -10)
        self.assertEqual(mul(2, -5), -10)
        self.assertEqual(mul(0, 6), 0)

    def test_div(self):
        self.assertEqual(div(10, 2), 5)
        self.assertEqual(div(-15, -3), 5)
        self.assertEqual(div(10, -2), -5)
        self.assertEqual(div(-10, 2), -5)
        self.assertEqual(div(0, 2), 0)

    def test_div_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            div(10, 0)


if __name__=="__main__":
    unittest.main()