import unittest
from unittest.mock import patch 
from AdvancedCalculator.advancedOperations import calculate_formula

class TestMainFunctions(unittest.TestCase):
    def test_calculate_formula(self):

        test_cases = [
            ("3 + 5 * 3  * (2 + 1)", 48),
            ("3 + 2 * (10 -  1 * 30)", -37)
        ]
        for input_text, expected_value in test_cases:
            self.assertEqual(calculate_formula(input_text), expected_value)



if __name__=="__main__":
    unittest.main()