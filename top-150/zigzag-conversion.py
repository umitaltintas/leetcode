class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        rows = [""] * numRows
        i = 0
        step = 1
        for c in s:
            rows[i] += c
            if i == 0:
                step = 1
            elif i == numRows - 1:
                step = -1
            i += step
        return "".join(rows)

import unittest
class TestSolution(unittest.TestCase):
    def test_convert_empty_string(self):
        s = Solution()
        self.assertEqual(s.convert("", 3), "")

    def test_convert_single_row(self):
        s = Solution()
        self.assertEqual(s.convert("PAYPALISHIRING", 1), "PAYPALISHIRING")

    def test_convert_two_rows(self):
        s = Solution()
        self.assertEqual(s.convert("PAYPALISHIRING", 2), "PYAIHRNAPLSIIG")

    def test_convert_three_rows(self):
        s = Solution()
        self.assertEqual(s.convert("PAYPALISHIRING", 3), "PAHNAPLSIIGYIR")

    def test_convert_four_rows(self):
        s = Solution()
        self.assertEqual(s.convert("PAYPALISHIRING", 4), "PINALSIGYAHRPI")

    def test_convert_five_rows(self):
        s = Solution()
        self.assertEqual(s.convert("PAYPALISHIRING", 5), "PHASIYIRPLIGAN")

    def test_convert_six_rows(self):
        s = Solution()
        self.assertEqual(s.convert("PAYPALISHIRING", 6), "PRAIIYHNPSGAIL")

if __name__ == '__main__':
    unittest.main()