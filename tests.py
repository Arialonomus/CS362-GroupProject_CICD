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


if __name__ == '__main__':
    unittest.main()
