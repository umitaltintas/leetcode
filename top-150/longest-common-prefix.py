class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs:
            return ""
        prefix = strs[0]
        for s in strs[1:]:
            while not s.startswith(prefix):
                prefix = prefix[:-1]
                if not prefix:
                    return ""
        return prefix
        
import unittest

class TestSolution(unittest.TestCase):
    def test_empty_list(self):
        s = Solution()
        self.assertEqual(s.longestCommonPrefix([]), "")

    def test_single_word(self):
        s = Solution()
        self.assertEqual(s.longestCommonPrefix(["hello"]), "hello")

    def test_no_common_prefix(self):
        s = Solution()
        self.assertEqual(s.longestCommonPrefix(["dog", "racecar", "car"]), "")

    def test_common_prefix(self):
        s = Solution()
        self.assertEqual(s.longestCommonPrefix(["flower", "flow", "flight"]), "fl")

    def test_all_same_word(self):
        s = Solution()
        self.assertEqual(s.longestCommonPrefix(["apple", "apple", "apple"]), "apple")

    def test_one_word_is_prefix(self):
        s = Solution()
        self.assertEqual(s.longestCommonPrefix(["apple", "app"]), "app")

if __name__ == '__main__':
    unittest.main()