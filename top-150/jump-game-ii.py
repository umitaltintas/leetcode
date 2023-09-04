class Solution:
    def jump(self, nums: list[int]) -> int:
        # Handle edge case of empty list
        if not nums:
            return -1

        # Initialize variables
        jumps = 0
        curr_end = 0
        curr_max = 0
        
        # Iterate through the array
        for i in range(len(nums) - 1):
            # Update the maximum index that can be reached from the current index
            curr_max = max(curr_max, i + nums[i])
            
            # If the current index is the end of the current jump, update the end of the current jump
            if i == curr_end:
                jumps += 1
                curr_end = curr_max
                
        # Return the minimum number of jumps to reach the last index
        return jumps
    
import unittest

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_empty_list(self):
        self.assertEqual(self.solution.jump([]), -1)

    def test_single_element_list(self):
        self.assertEqual(self.solution.jump([0]), 0)

    def test_two_element_list(self):
        self.assertEqual(self.solution.jump([2, 1]), 1)

    def test_three_element_list(self):
        self.assertEqual(self.solution.jump([1, 2, 1]), 2)

    def test_four_element_list(self):
        self.assertEqual(self.solution.jump([2, 3, 1, 1, 4]), 2)

    def test_five_element_list(self):
        self.assertEqual(self.solution.jump([1, 2, 3, 4, 5]), 3)

    def test_six_element_list(self):
        self.assertEqual(self.solution.jump([5, 4, 3, 2, 1, 0]), 1)

if __name__ == '__main__':
    unittest.main()