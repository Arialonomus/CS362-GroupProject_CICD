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


if __name__ == '__main__':
    unittest.main()
