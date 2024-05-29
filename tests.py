import unittest
from task import conv_num


class TestConvNum(unittest.TestCase):
    """Test that the function returns None for non-string values"""
    def test1(self):
        test_case = 1
        self.assertEqual(conv_num(test_case), None)


if __name__ == '__main__':
    unittest.main()
