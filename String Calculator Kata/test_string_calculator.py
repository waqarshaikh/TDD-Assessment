import unittest
import string_calulator

class TestStringCalculator(unittest.TestCase):
    def test_add(self):
        # test empty string return 0
        self.assertEqual(string_calulator.add(""), 0)
        
        # test one number return the number
        self.assertEqual(string_calulator.add("1"), 1) 

        # test two numbers return their sum
        self.assertEqual(string_calulator.add("1,2"), 3) 

        # test multiple numbers return their sum
        self.assertEqual(string_calulator.add("10,20,30"), 60) 

        # test handle new lines between numbers
        self.assertEqual(string_calulator.add("1\n2,3"), 6)

        # test support different delimiters
        self.assertEqual(string_calulator.add("//;\n1;2"), 3)


if __name__ == "__main__":
    unittest.main()
