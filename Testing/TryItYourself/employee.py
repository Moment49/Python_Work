class Employee:
    """A class to model an employee"""

    def __init__(self, first, last, annual_salary):
        """Initialize first and last name, annual salary"""
        self.first = first
        self.last = last
        self.annual_salary = annual_salary
    
    def give_raise(self, give_raise=5000):
        """Give salary raise"""
        if give_raise == 5000:
            self.annual_salary += give_raise
        else:
            self.annual_salary += give_raise
            
        return self.annual_salary