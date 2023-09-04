class Solution:
    def hIndex(self, citations: list[int]) -> int:
        n = len(citations)
        dp = [0] * (n + 1)
        total = 0
        
        for c in citations:
            if c >= n:
                dp[n] += 1
            else:
                dp[c] += 1
        
        for i in range(n, -1, -1):
            total += dp[i]
            if total >= i:
                return i
        
        return 0
    

import unittest

class TestHIndex(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
        
    def test_empty_list(self):
        self.assertEqual(self.solution.hIndex([]), 0)
    
    def test_single_citation(self):
        self.assertEqual(self.solution.hIndex([0]), 0)
        self.assertEqual(self.solution.hIndex([1]), 1)
        self.assertEqual(self.solution.hIndex([2]), 1)
    
    def test_multiple_citations(self):
        self.assertEqual(self.solution.hIndex([0, 0, 0]), 0)
        self.assertEqual(self.solution.hIndex([1, 1, 1]), 1)
        self.assertEqual(self.solution.hIndex([2, 2, 2]), 2)
        self.assertEqual(self.solution.hIndex([3, 3, 3]), 3)
        self.assertEqual(self.solution.hIndex([0, 1, 2]), 1)
        self.assertEqual(self.solution.hIndex([0, 1, 3]), 1)
        self.assertEqual(self.solution.hIndex([0, 2, 3]), 2)
        self.assertEqual(self.solution.hIndex([1, 2, 3]), 2)
        self.assertEqual(self.solution.hIndex([0, 1, 2, 3]), 2)
        self.assertEqual(self.solution.hIndex([0, 1, 2, 4]), 2)
        self.assertEqual(self.solution.hIndex([0, 1, 3, 5, 6]), 3)
    
    def test_large_list(self):
        citations = [i for i in range(100000)]
        self.assertEqual(self.solution.hIndex(citations), 50000)
    
    def test_out_of_bounds_citations(self):
        self.assertEqual(self.solution.hIndex([4, 5, 6]), 3)
        self.assertEqual(self.solution.hIndex([0, 1, 100]), 1)
        self.assertEqual(self.solution.hIndex([0, 1, 1000]), 1)
        self.assertEqual(self.solution.hIndex([0, 1, 10000]), 1)
        self.assertEqual(self.solution.hIndex([0, 1, 100000]), 1)

if __name__ == '__main__':
    unittest.main()