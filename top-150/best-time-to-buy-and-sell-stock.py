class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        if not prices:
            return 0

        min_price = prices[0]
        max_profit = 0
        for i in range(1, len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]
            else:
                max_profit = max(max_profit, prices[i] - min_price)

        return max_profit


import unittest


class TestSolution(unittest.TestCase):
    def test_maxProfit(self):
        s = Solution()
        self.assertEqual(s.maxProfit([7, 1, 5, 3, 6, 4]), 5)
        self.assertEqual(s.maxProfit([7, 6, 4, 3, 1]), 0)
        self.assertEqual(s.maxProfit([1, 2, 3, 4, 5]), 4)
        self.assertEqual(s.maxProfit([2, 4, 1]), 2)


if __name__ == "__main__":
    unittest.main()
