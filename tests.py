import unittest
from task import conv_num


class TestConvNum(unittest.TestCase):
    """Test that conv_num returns None for non-string values"""
    def test1(self):
        test_case = 1
        expected_val = None
        self.assertEqual(conv_num(test_case), expected_val)

    """Test that conv_num returns None for the empty string"""
    def test2(self):
        test_case = ''
        expected_val = None
        self.assertEqual(conv_num(test_case), expected_val)

    """Test that conv_num returns None for strings with multiple decimals"""
    def test3(self):
        test_case = '12.3.45'
        expected_val = None
        self.assertEqual(conv_num(test_case), expected_val)

    """Test that conv_num returns None for non-hex strings
    containing non-numeric, non-decmial characters"""
    def test4(self):
        test_case = '12345A'
        expected_val = None
        self.assertEqual(conv_num(test_case), expected_val)

    """Test that conv_num rejects negative strings contraining more than one
    negative symbol"""
    def test5(self):
        test_case = '-12345-'
        expected_val = None
        self.assertEqual(conv_num(test_case), expected_val)

    """Test that conv_num properly converts strings to the equivalent
    non-negative decimal integer"""
    def test6(self):
        test_case = '12345'
        expected_val = 12345
        self.assertEqual(conv_num(test_case), expected_val)

    """Test that conv_num properly converts negative digit strings to the
    equivalent integer"""
    def test7(self):
        test_case = '-98765'
        expected_val = -98765
        self.assertEqual(conv_num(test_case), expected_val)

    """Test that conv_num properly converts rational decimal strings
    to the equivalent floating point number"""
    def test8(self):
        test_case = '-123.45'
        expected_val = -123.45
        self.assertEqual(conv_num(test_case), expected_val)

    """Test that conv_num properly converts float values without a
    leading zero"""
    def test9(self):
        test_case = '.45'
        expected_val = 0.45
        self.assertEqual(conv_num(test_case), expected_val)

    """Test that conv_num properly converts float values without a
    trailing zero"""
    def test10(self):
        test_case = '123.'
        expected_val = 123.0
        self.assertEqual(conv_num(test_case), expected_val)

    """Test that conv_num properly converts hexadecimal values to
    decimal integers"""
    def test11(self):
        test_case = '0xAD4'
        expected_val = 2772
        self.assertEqual(conv_num(test_case), expected_val)

    """Test that conv_num properly converts case-insensitive
    hexadecimal values to decimal integers"""
    def test12(self):
        test_case = '0Xad4'
        expected_val = 2772
        self.assertEqual(conv_num(test_case), expected_val)

    """Test that conv_num properly returns None for hexadecimal
    strings containing invalid alphabetic symbols"""
    def test13(self):
        test_case = '0xAZ4'
        expected_val = None
        self.assertEqual(conv_num(test_case), expected_val)

    """Test that conv_num properly returns None for fractional
    hexadecmial strings"""
    def test14(self):
        test_case = '0xAD4.1'
        expected_val = None
        self.assertEqual(conv_num(test_case), expected_val)

    """Test that conv_num properly converts negative hexadecimal
    values to decimal integers"""
    def test15(self):
        test_case = '-0xFF'
        expected_val = -255
        self.assertEqual(conv_num(test_case), expected_val)


if __name__ == '__main__':
    unittest.main()
