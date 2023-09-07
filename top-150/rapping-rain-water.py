class Solution:
    def trap(self, height: list[int]) -> int:
        total = 0
        max=max = [0] * len(height)
        
        local_max = 0
        for i in range(len(height)):
            if height[i] > local_max:
                local_max = height[i]
            max[i] = local_max
    #    biggest values on right side
        local_max = 0
        for i in range(len(height) - 1, -1, -1):
            if height[i] > local_max:
                local_max = height[i]
            max[i] = min(local_max, max[i])
            
        for i in range(len(height)):
            total += max[i] - height[i]
            
        
        return total

import unittest
class TestTrap(unittest.TestCase):
    def test_trap_empty(self):
        s = Solution()
        self.assertEqual(s.trap([]), 0)
        
    def test_trap_single(self):
        s = Solution()
        self.assertEqual(s.trap([5]), 0)
        
    def test_trap_two(self):
        s = Solution()
        self.assertEqual(s.trap([5, 3]), 0)
        
    def test_trap_three(self):
        s = Solution()
        self.assertEqual(s.trap([5, 3, 2]), 0)
        
    def test_trap_four(self):
        s = Solution()
        self.assertEqual(s.trap([5, 3, 2, 4]), 3)
        
    def test_trap_five(self):
        s = Solution()
        self.assertEqual(s.trap([5, 3, 2, 4, 1]), 3)
        
    def test_trap_six(self):
        s = Solution()
        self.assertEqual(s.trap([5, 3, 2, 4, 1, 2]), 4)
        
if __name__ == '__main__':
    unittest.main()