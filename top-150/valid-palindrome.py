class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        left, right = 0, len(s) - 1
        isalnum = str.isalnum

        while left < right:
            while left < right and not isalnum(s[left]):
                left += 1

            while left < right and not isalnum(s[right]):
                right -= 1

            if s[left] != s[right]:
                return False

            left += 1
            right -= 1
        
        return True


import unittest

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_empty_string(self):
        self.assertTrue(self.solution.isPalindrome(""))

    def test_single_character(self):
        self.assertTrue(self.solution.isPalindrome("a"))

    def test_palindrome(self):
        self.assertTrue(self.solution.isPalindrome("A man a plan a canal Panama"))

    def test_non_palindrome(self):
        self.assertFalse(self.solution.isPalindrome("race a car"))

    def test_punctuation(self):
        self.assertTrue(self.solution.isPalindrome("A man, a plan, a canal: Panama"))

    def test_whitespace(self):
        self.assertTrue(self.solution.isPalindrome("A man a plan a canal Panama"))

    def test_mixed_case(self):
        self.assertTrue(self.solution.isPalindrome("A man a plan a canal Panama"))

    def test_numbers(self):
        self.assertTrue(self.solution.isPalindrome("12321"))

    def test_special_characters(self):
        self.assertTrue(self.solution.isPalindrome("!@#$%^&*()_+-=[]{}|;':\",./<>?\\"))

if __name__ == "__main__":
    unittest.main()