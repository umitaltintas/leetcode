class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        i = m - 1
        j = n - 1

        for k in range(m + n - 1, -1, -1):
            nums1[k], nums1[k - 1] = (
                (nums1[i], nums2[j]) if nums1[i] > nums2[j] else (nums2[j], nums1[i])
            )
            if i == 0 or j == 0:
                break
            else:
                j = j - 1
                i = i - 1
        if i == 0:
            for k in range(j):
                nums1[k] = nums2[k]


import unittest


class TestSolution(unittest.TestCase):
    def test_merge(self):
        sol = Solution()

        # Test case 1
        nums1 = [1, 2, 3, 0, 0, 0]
        m = 3
        nums2 = [2, 5, 6]
        n = 3
        sol.merge(nums1, m, nums2, n)
        self.assertEqual(nums1, [1, 2, 2, 3, 5, 6])

        # Test case 2
        nums1 = [1]
        m = 1
        nums2 = []
        n = 0
        sol.merge(nums1, m, nums2, n)
        self.assertEqual(nums1, [1])

        # Test case 3
        nums1 = [0]
        m = 0
        nums2 = [1]
        n = 1
        sol.merge(nums1, m, nums2, n)
        self.assertEqual(nums1, [1])

        # Test case 4
        nums1 = [4, 5, 6, 0, 0, 0]
        m = 3
        nums2 = [1, 2, 3]
        n = 3
        sol.merge(nums1, m, nums2, n)
        self.assertEqual(nums1, [1, 2, 3, 4, 5, 6])

        # Test case 5
        nums1 = [1, 2, 3, 0, 0, 0]
        m = 3
        nums2 = [4, 5, 6]
        n = 3
        sol.merge(nums1, m, nums2, n)
        self.assertEqual(nums1, [1, 2, 3, 4, 5, 6])


if __name__ == "__main__":
    unittest.main()
