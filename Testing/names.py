import unittest
from name_func import get_formatted_name

class NamesTestCases(unittest.TestCase):
    """Tests for name_func.py"""

    def test_first_last_name(self):
        """Do names like 'Elvis Ibenacho work?'"""
        

print("Enter 'q' at any time to quit.")

while True:
    first = input("\nPlease give me a first name: ")
    if first == 'q':
        break
    last = input("Please give me a last name: ")
    if last == 'q':
        break
    
formatted_name = get_formatted_name(first, last)
print(f"\tNeatly formatted name: {formatted_name}")