# 11.1 & 11.2
import unittest
from city_func import get_country_info

class CitiesTestCases(unittest.TestCase):
    """Test for city_func.py"""

    def test_city_country(self):
        """Do country info like 'Santiago, Chile'"""
        formatted_country_info = get_country_info('toronto', 'canada')
        self.assertEqual(formatted_country_info, 'Toronto, Canada')


    def test_city_country_population(self):
        """Do country info like 'Santiago, Chile - population 5000000'"""
        formatted_country_info = get_country_info('toronto', 'canada', '5000000')
        self.assertEqual(formatted_country_info, 'Toronto, Canada - Population=5000000')
        




if __name__ == '__main__':
    unittest.main()