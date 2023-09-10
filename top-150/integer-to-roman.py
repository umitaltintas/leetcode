class Solution:
    def intToRoman(self, num: int) -> str:
        symbols = {
            'I': 1,
            'IV': 4,
            'V': 5,
            'IX': 9,
            'X': 10,
            'XL': 40,
            'L': 50,
            'XC': 90,
            'C': 100,
            'CD': 400,
            'D': 500,
            'CM': 900,
            'M': 1000,
        }
        
        roman = ''
        for symbol, value in reversed(symbols.items()):
            while num >= value:
                roman += symbol
                num -= value
                
        return roman
    
import unittest
class TestIntToRoman(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_single_symbol(self):
        self.assertEqual(self.solution.intToRoman(1), "I")
        self.assertEqual(self.solution.intToRoman(5), "V")
        self.assertEqual(self.solution.intToRoman(10), "X")
        self.assertEqual(self.solution.intToRoman(50), "L")
        self.assertEqual(self.solution.intToRoman(100), "C")
        self.assertEqual(self.solution.intToRoman(500), "D")
        self.assertEqual(self.solution.intToRoman(1000), "M")

    def test_multiple_symbols(self):
        self.assertEqual(self.solution.intToRoman(3), "III")
        self.assertEqual(self.solution.intToRoman(58), "LVIII")
        self.assertEqual(self.solution.intToRoman(1994), "MCMXCIV")

   

if __name__ == '__main__':
    unittest.main()
    
