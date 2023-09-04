class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        products = [1] * n
        for i in range(1, n):
            products[i] = products[i-1] * nums[i-1]
        right_product = 1
        for i in range(n-1, -1, -1):
            products[i] *= right_product
            right_product *= nums[i]
        return products

import unittest

class Test(unittest.TestCase):
    def test_product_except_self(self):
        solution = Solution()
        self.assertEqual(solution.productExceptSelf([1,2,3,4]), [24,12,8,6])
    def test_product_except_self_2(self):
        solution = Solution()
        self.assertEqual(solution.productExceptSelf([0,0]), [0,0])
        
    def test_product_except_self_3(self):
        solution = Solution()
        self.assertEqual(solution.productExceptSelf([0,1]), [1,0])
        
          
        
if __name__ == '__main__':
    unittest.main()