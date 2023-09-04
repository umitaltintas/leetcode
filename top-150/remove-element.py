class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        i = 0

        for j in range(len(nums)):
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1

        return i


import unittest


class TestSolution(unittest.TestCase):
    def test_removeElement_emptyList(self):
        s = Solution()
        nums = []
        val = 1
        self.assertEqual(s.removeElement(nums, val), 0)

    def test_removeElement_singleElement(self):
        s = Solution()
        nums = [1]
        val = 1
        self.assertEqual(s.removeElement(nums, val), 0)

    def test_removeElement_twoDistinctElements(self):
        s = Solution()
        nums = [1, 2]
        val = 1
        self.assertEqual(s.removeElement(nums, val), 1)

    def test_removeElement_twoIdenticalElements(self):
        s = Solution()
        nums = [1, 1]
        val = 1
        self.assertEqual(s.removeElement(nums, val), 0)

    def test_removeElement_multipleIdenticalElements(self):
        s = Solution()
        nums = [1, 1, 2, 2, 2, 3]
        val = 2
        self.assertEqual(s.removeElement(nums, val), 3)

    def test_removeElement_allIdenticalElements(self):
        s = Solution()
        nums = [1, 1, 1, 1, 1]
        val = 1
        self.assertEqual(s.removeElement(nums, val), 0)


if __name__ == "__main__":
    unittest.main()
