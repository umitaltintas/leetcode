class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i:i+len(needle)] == needle: return i
        return -1

import unittest
class TestSolution(unittest.TestCase):
    def test_strStr_empty_haystack(self):
        s = Solution()
        self.assertEqual(s.strStr("", "hello"), -1)

    def test_strStr_empty_needle(self):
        s = Solution()
        self.assertEqual(s.strStr("hello", ""), 0)

    def test_strStr_needle_longer_than_haystack(self):
        s = Solution()
        self.assertEqual(s.strStr("hello", "hello world"), -1)

    def test_strStr_needle_not_in_haystack(self):
        s = Solution()
        self.assertEqual(s.strStr("hello", "world"), -1)

    def test_strStr_needle_in_haystack(self):
        s = Solution()
        self.assertEqual(s.strStr("hello", "ll"), 2)

    def test_strStr_needle_at_beginning_of_haystack(self):
        s = Solution()
        self.assertEqual(s.strStr("hello", "he"), 0)

    def test_strStr_needle_at_end_of_haystack(self):
        s = Solution()
        self.assertEqual(s.strStr("hello", "lo"), 3)

if __name__ == '__main__':
    unittest.main()