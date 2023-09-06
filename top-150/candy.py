class Solution:
    def candy(self, ratings: list[int]) -> int:
        """
        Given a list of student ratings, return the minimum number of candies needed to distribute
        following these rules:
        - Every student gets at least 1 candy
        - Students with higher ratings get more candies than their neighbors

        Args:
          ratings (list[int]): List of integer ratings for each student

        Returns:
          int: Minimum number of candies needed
        """

        n = len(ratings)
        candies = [1] * n

        # Traverse the ratings from left to right.
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1

        # Traverse the ratings from right to left.
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                candies[i] = max(candies[i], candies[i + 1] + 1)

        return sum(candies)


import unittest


class TestCandy(unittest.TestCase):
    def test_basic(self):
        ratings = [1, 2, 3]
        expected = [1, 2, 3]
        sol = Solution()
        result = sol.candy(ratings)
        self.assertEqual(result, sum(expected))

    def test_descending(self):
        ratings = [3, 2, 1]
        expected = [3, 2, 1]
        sol = Solution()
        result = sol.candy(ratings)
        self.assertEqual(result, sum(expected))

    def test_peak(self):
        ratings = [1, 3, 2, 1]
        expected = [1, 3, 2, 1]
        sol = Solution()
        result = sol.candy(ratings)
        self.assertEqual(result, sum(expected))

    def test_valley(self):
        ratings = [1, 2, 1]
        expected = [1, 2, 1]
        sol = Solution()
        result = sol.candy(ratings)
        self.assertEqual(result, sum(expected))


if __name__ == "__main__":
    unittest.main()
