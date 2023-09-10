class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        length = 0
        a=s.split()
        if len(a)==0:
            return 0
        else:
            length=len(a[-1])
            
        return length
    
import unittest

class Test(unittest.TestCase):
    solution = Solution()
    def test_length_of_last_word(self):
        self.assertEqual(self.solution.lengthOfLastWord("Hello World"), 5)
        self.assertEqual(self.solution.lengthOfLastWord("   fly me   to   the moon  "), 4)
        self.assertEqual(self.solution.lengthOfLastWord("luffy is still joyboy"), 6)
        self.assertEqual(self.solution.lengthOfLastWord("a"), 1)
        self.assertEqual(self.solution.lengthOfLastWord("a "),1)
        self.assertEqual(self.solution.lengthOfLastWord("b   a    "), 1)
        self.assertEqual(self.solution.lengthOfLastWord("Today is a nice day"), 3)

if __name__ == '__main__':
    unittest.main()