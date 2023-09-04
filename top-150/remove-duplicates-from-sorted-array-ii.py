class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        length = len(nums)
        if length < 2:
            return length
        j = 0
        k = 0

        for i in range(length - 1):
            if nums[i + 1] == nums[j]:
                k += 1
                if k < 2:
                    j += 1
                nums[j] = nums[i + 1]

            else:
                nums[j + 1] = nums[i + 1]
                k = 0
                j += 1
        return j + 1


import unittest


class TestSolution(unittest.TestCase):
    def test_removeDuplicates_emptyList(self):
        s = Solution()
        nums = []
        self.assertEqual(s.removeDuplicates(nums), 0)

    def test_removeDuplicates_singleElement(self):
        s = Solution()
        nums = [1]
        self.assertEqual(s.removeDuplicates(nums), 1)

    def test_removeDuplicates_twoDistinctElements(self):
        s = Solution()
        nums = [1, 2]
        self.assertEqual(s.removeDuplicates(nums), 2)

    def test_removeDuplicates_twoIdenticalElements(self):
        s = Solution()
        nums = [1, 1]
        self.assertEqual(s.removeDuplicates(nums), 2)

    def test_removeDuplicates_threeIdenticalElements(self):
        s = Solution()
        nums = [1, 1, 1]
        self.assertEqual(s.removeDuplicates(nums), 2)

    def test_removeDuplicates_multipleIdenticalElements(self):
        s = Solution()
        nums = [1, 1, 2, 2, 2, 3]
        self.assertEqual(s.removeDuplicates(nums), 5)

    def test_removeDuplicates_allIdenticalElements(self):
        s = Solution()
        nums = [1, 1, 1, 1, 1]
        self.assertEqual(s.removeDuplicates(nums), 2)


if __name__ == "__main__":
    unittest.main()
