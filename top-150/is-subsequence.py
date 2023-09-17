class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        for i in range(len(s)):
            for j in range(len(t)):
                if s[i] == t[j]:
                    t = t[j+1:]
                    break
            else:
                return False
        return True
    
            
            
                

import unittest

class TestSolution(unittest.TestCase):
    
    def setUp(self):
        self.solution = Solution()
        
    def test_empty_string(self):
        self.assertTrue(self.solution.isSubsequence("", ""))
    
    def test_empty_substring(self):
        self.assertTrue(self.solution.isSubsequence("", "abc"))
    
    def test_empty_string(self):
        self.assertFalse(self.solution.isSubsequence("abc", ""))
    
    def test_substring_at_beginning(self):
        self.assertTrue(self.solution.isSubsequence("abc", "abc"))
    
    def test_substring_at_end(self):
        self.assertTrue(self.solution.isSubsequence("abc", "xyzabc"))
    
    def test_substring_in_middle(self):
        self.assertTrue(self.solution.isSubsequence("abc", "xyzabc123"))
    
    def test_substring_not_present(self):
        self.assertFalse(self.solution.isSubsequence("abc", "xyz123"))
    
    def test_substring_repeated(self):
        self.assertTrue(self.solution.isSubsequence("abc", "xyzabcabc123"))
    
    def test_example_1(self):
        self.assertTrue(self.solution.isSubsequence("abc", "ahbgdc"))
    
    def test_example_2(self):
        self.assertFalse(self.solution.isSubsequence("axc", "ahbgdc"))
   
        
if __name__ == "__main__":
    unittest.main()
    