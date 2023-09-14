class Solution:
    def reverseWords(self, s: str) -> str:
        words=s.split()
        # join by space
        return " ".join(words[::-1])

import unittest
class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_reverseWords_empty_string(self):
        self.assertEqual(self.solution.reverseWords(""), "")

    def test_reverseWords_single_word(self):
        self.assertEqual(self.solution.reverseWords("hello"), "hello")

    def test_reverseWords_multiple_words(self):
        self.assertEqual(self.solution.reverseWords("hello world"), "world hello")

    def test_reverseWords_multiple_spaces(self):
        self.assertEqual(self.solution.reverseWords("  hello   world  "), "world hello")

    def test_reverseWords_leading_trailing_spaces(self):
        self.assertEqual(self.solution.reverseWords("  hello world  "), "world hello")

    def test_reverseWords_unicode_characters(self):
        self.assertEqual(self.solution.reverseWords("héllo wórld"), "wórld héllo")

if __name__ == '__main__':
    unittest.main()