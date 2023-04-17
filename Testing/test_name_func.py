import unittest
from name_func import get_formatted_name

class NamesTestCases(unittest.TestCase):
    """Tests for name_func.py"""

    def test_first_last_name(self):
        """Do names like 'Elvis Ibenacho work?'"""
        formatted_name = get_formatted_name('Elvis', 'Ibenacho')
        self.assertEqual(formatted_name, 'Elvis Ibenacho')
    
    def test_first_last_middle(self):
        """Do names like 'Elvis Chimdi Ibenacho work?'"""
        formatted_name = get_formatted_name(
            'Elvis', 'Ibenacho', 'Chimdi')
        self.assertEqual(formatted_name, 'Elvis Chimdi Ibenacho')
        


if __name__ == '__main__':
    unittest.main()