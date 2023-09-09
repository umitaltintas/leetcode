class Solution:
    def romanToInt(self, s: str) -> int:
        symbols = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }
        total=0
        for i in range(len(s)):
            if i < len(s) - 1 and symbols[s[i]] < symbols[s[i+1]]:
                total -= symbols[s[i]]
            else:
                total += symbols[s[i]]
            # If a symbol occuer before a symbol that bigger than it it should be substructed from total
            
        return total

import unittest

class TestRomanToInt(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_single_symbol(self):
        self.assertEqual(self.solution.romanToInt("I"), 1)
        self.assertEqual(self.solution.romanToInt("V"), 5)
        self.assertEqual(self.solution.romanToInt("X"), 10)
        self.assertEqual(self.solution.romanToInt("L"), 50)
        self.assertEqual(self.solution.romanToInt("C"), 100)
        self.assertEqual(self.solution.romanToInt("D"), 500)
        self.assertEqual(self.solution.romanToInt("M"), 1000)

    def test_multiple_symbols(self):
        self.assertEqual(self.solution.romanToInt("III"), 3)
        self.assertEqual(self.solution.romanToInt("LVIII"), 58)
        self.assertEqual(self.solution.romanToInt("MCMXCIV"), 1994)

    def test_invalid_input(self):
        self.assertEqual(self.solution.romanToInt(""), 0)
        self.assertEqual(self.solution.romanToInt("IIII"), 4)
        self.assertEqual(self.solution.romanToInt("VV"), 10)
        self.assertEqual(self.solution.romanToInt("XXXX"), 40)
        self.assertEqual(self.solution.romanToInt("LL"), 100)
        self.assertEqual(self.solution.romanToInt("CCCC"), 400)
        self.assertEqual(self.solution.romanToInt("DD"), 1000)
        self.assertEqual(self.solution.romanToInt("MMMM"), 4000)

if __name__ == '__main__':
    unittest.main()