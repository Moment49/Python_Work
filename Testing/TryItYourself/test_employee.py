import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    """Tests for the class Employee"""

    def setUp(self):
        """
        Create a set of test cases for a given salary raise
        """
        self.employee_1 = Employee('Elvis', 'Ibenacho', 50000)

    def test_give_default_raise(self):
        """Test that the default raise is given "5000" """
        employee_raise = self.employee_1.give_raise()
        self.assertEqual(55000, employee_raise)
    
    def test_give_custom_raise(self):
        """Test a custom salary raise"""
        employee_raise = self.employee_1.give_raise(4000)
        self.assertEqual(54000, employee_raise)



if __name__ == '__main__':
    unittest.main()
        