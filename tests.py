import unittest
from task import conv_num, my_datetime


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

    """Test that conv_num properly returns None for hexadecimal
    strings without the 0x prefix"""
    def test16(self):
        test_case = 'AD4'
        expected_val = None
        self.assertEqual(conv_num(test_case), expected_val)
        

class TestDate(unittest.TestCase):
    """
    Tests for my_datetime(num_sec) function in task.py
    """
    
    def test1(self):
        """
        Test that function properly returns start date when input is 0
        """
        val = 0
        expected = '01-01-1970'
        self.assertEqual(my_datetime(val), expected)
    
    def test2(self):
        """
        Test leap year value
        """
        val = 1716120000
        expected = '05-19-2024'
        self.assertEqual(my_datetime(val), expected)
        
    def test3(self):
        """
        Test a regular year
        """
        val = 32503723200
        expected = '01-01-3000'
        self.assertEqual(my_datetime(val), expected)
        
    def test4(self):
        """
        Test edge of year case
        """
        val = 946684799
        expected = '12-31-1999'
        self.assertEqual(my_datetime(val), expected)
    
    def test5(self):
        """
        Tests that the function properly handles and returns expected date
        of a large value
        """
        val = 221858827200
        expected = '06-05-9000'
        self.assertEqual(my_datetime(val), expected)

if __name__ == '__main__':
    unittest.main()
