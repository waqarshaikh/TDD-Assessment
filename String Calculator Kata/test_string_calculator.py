import unittest
import string_calulator

class TestStringCalculator(unittest.TestCase):
    def test_add(self):
        # test empty string return 0
        self.assertEqual(string_calulator.add(""), 0)
        
        # test one number return the number
        self.assertEqual(string_calulator.add("1"), 1) 

if __name__ == "__main__":
    unittest.main()
