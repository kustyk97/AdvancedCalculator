import unittest
from unittest.mock import patch 
from AdvancedCalculator.utils import is_float, is_int, try_get_float_value, are_parentheses_matched, is_only_floats, is_enable_chars, is_last_num_or_bracket, is_formula


class TestMainFunctions(unittest.TestCase):
    def test_is_float(self):
        test_cases = ["5.0", "7", "-3", "-3.5", "0", "-0", "-0.0", "0.0"]
        for test_case in test_cases:
            self.assertTrue(is_float(test_case))

        self.assertFalse(is_float("test"))
        self.assertFalse(is_float("-20t"))

    def test_is_int(self):
        self.assertTrue(is_int("5"))
        self.assertTrue(is_int("-3"))
        self.assertTrue(is_int("0"))
        self.assertFalse(is_int("10.0"))
        self.assertFalse(is_int("str"))
        self.assertFalse(is_int("4t"))


    @patch('builtins.print')
    def test_valid_float_input(self, mock_print):
        test_cases = [
            ('3.14', 3.14),
            ('-3.14', -3.14),
            ('0', 0.0),
            ('1e10', 1e10),
            ('-1e10', -1e10),
            ('1.7976931348623157e+308', 1.7976931348623157e+308),
            ('5e-324', 5e-324) 
        ]
        
        for input_value, expected_output in test_cases:
            with patch('builtins.input', return_value=input_value):
                result = try_get_float_value()
                self.assertEqual(result, expected_output)
                mock_print.assert_not_called()

    @patch('builtins.print')
    def test_invalid_float_input(self, mock_print):
        test_cases = ["abc", "test", "", "10-"]
        for input_value in test_cases:
            with patch("builtins.input", return_value=input_value):
                result = try_get_float_value()
                self.assertIsNone(result)
                mock_print.assert_called()

    def test_are_parentheses_matched(self):
        self.assertTrue(are_parentheses_matched("(1+2)"))
        self.assertTrue(are_parentheses_matched("2 + 3"))
        self.assertTrue(are_parentheses_matched("(3 + 1)(1-2)"))
        self.assertTrue(are_parentheses_matched("(2(2+1))"))
        self.assertTrue(are_parentheses_matched("3"))

        self.assertFalse(are_parentheses_matched("(3+1"))
        self.assertFalse(are_parentheses_matched("(3+(1)"))
        self.assertFalse(are_parentheses_matched("(3+1))"))
    
    def test_is_only_floats(self):
        
        self.assertTrue(is_only_floats(["10" "10.0", ""]))
        
        self.assertFalse(is_only_floats(["s"]))
        
    def test_is_enable_chars(self):
        self.assertTrue(is_enable_chars("4 + 3(2-1/3)"))

        self.assertFalse(is_enable_chars("4 + 3(2-1/3)s"))

    def test_is_last_num_or_bracket(self):
        
        self.assertTrue(is_last_num_or_bracket("32"))
        self.assertTrue(is_last_num_or_bracket("32)"))
        self.assertFalse(is_last_num_or_bracket("32+"))
        self.assertFalse(is_last_num_or_bracket("32-"))
        self.assertFalse(is_last_num_or_bracket("33s"))
        
    def test_is_formula(self):
        self.assertTrue(is_formula("3 + 1(3*2/4)"))
        self.assertFalse(is_formula("3 + 1(3*2/4)s"))
        self.assertFalse(is_formula("3 + -1(3*2/4)"))
        self.assertFalse(is_formula("3 + 1(3*2/4))"))
        self.assertFalse(is_formula("3 + 3 1(3*2/4))"))


if __name__=="__main__":
    unittest.main()