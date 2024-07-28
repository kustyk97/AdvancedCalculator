import unittest
from unittest.mock import patch 
from AdvancedCalculator.advancedOperations import calculate, get_id_of_open_bracket, get_id_of_close_bracket, try_get_list_of_brackets, convert_to_list, calculate_formula

class TestMainFunctions(unittest.TestCase):
    def test_calculate_formula_basic_operations(self):
        test_cases = [
            ("3 + 5 * 3 (2 + 1)", 48),
            ("3 + 2 (10 - 1 * 30)", -37),
            ("3 + 2", 5),
            ("3 * 2", 6)
        ]
        for input_text, expected_value in test_cases:
            with self.subTest(input_text=input_text, expected_value=expected_value):
                self.assertEqual(calculate(input_text), expected_value)

    def test_calculate_formula_edge_cases(self):
        test_cases = [
            ("0", 0),
            ("1 + 1", 2),
            ("1 + 2", 3),
            # ("3 (2 + 3) / 5", 3),
            # ("1(3 + 5) + 2", 16)
        ]
        for input_text, expected_value in test_cases:
            with self.subTest(input_text=input_text, expected_value=expected_value):
                self.assertEqual(calculate(input_text), expected_value)

    def test_get_id_of_open_bracket(self):
        self.assertEqual(get_id_of_open_bracket(['(', '1', '+', '2', ')']), 0)
        self.assertEqual(get_id_of_open_bracket(['1', '+', '(', '2', ')']), 2)
        self.assertIsNone(get_id_of_open_bracket(['1', '+', '2']))

    def test_get_id_of_close_bracket(self):
        self.assertEqual(get_id_of_close_bracket(['(', '1', '+', '2', ')']), 4)
        self.assertEqual(get_id_of_close_bracket(['(', '(', '1', ')', '+', '2', ')']), 6)
        self.assertIsNone(get_id_of_close_bracket(['1', '+', '2']))

    def test_try_get_list_of_brackets(self):
        self.assertEqual(try_get_list_of_brackets(['(', '1', '+', '2', ')']), [(0, 5)])
        self.assertEqual(try_get_list_of_brackets(['(', '1', '+', '(', '2', ')', ')']), [(0, 7)])
        self.assertEqual(try_get_list_of_brackets(['(', '1', '+', '(', '2', ')', ')', '(', '2', '+', '3', ')']), [(0, 7), (7, 12)])
        self.assertEqual(try_get_list_of_brackets(['1', '+', '2']), [])

    def test_convert_to_list(self):
        self.assertEqual(convert_to_list("1+2"), ['1', '+', '2'])
        self.assertEqual(convert_to_list("(3*4)-5"), ['(', '3', '*', '4', ')', '-', '5'])
        self.assertEqual(convert_to_list("10/2"), ['10', '/', '2'])

    def test_calculate_formula(self):
        self.assertEqual(calculate_formula(['1', '+', '2']), ['3.0'])
        self.assertEqual(calculate_formula(['2', '*', '3']), ['6.0'])
        self.assertEqual(calculate_formula(['6', '/', '2']), ['3.0'])
        self.assertEqual(calculate_formula(['3', '-', '1']), ['2.0'])
        self.assertEqual(calculate_formula(['1', '+', '2', '*', '3']), ['7.0'])
        self.assertEqual(calculate_formula(['6', '/', '2', '-', '1']), ['2.0'])
        self.assertEqual(calculate_formula(['2', '+', '2', '*', '2']), ['6.0'])
        self.assertEqual(calculate_formula(['2', '+', '3', '*', '4']), ['14.0'])
        self.assertEqual(calculate_formula(['10', '-', '2', '*', '3']), ['4.0'])
        self.assertEqual(calculate_formula(['12', '/', '3', '+', '4']), ['8.0'])


if __name__=="__main__":
    unittest.main()