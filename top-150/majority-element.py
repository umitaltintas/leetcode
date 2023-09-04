class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        l = len(nums)

        dict = {}

        for i in range(l):
            if nums[i] in dict:
                dict[nums[i]] += 1
            else:
                dict[nums[i]] = 1

        m = 0
        for i in dict:
            if dict[i] > l // 2:
                m = i
                break
        return m


import unittest


class TestSolution(unittest.TestCase):
    def test_majorityElement_singleElement(self):
        s = Solution()
        self.assertEqual(s.majorityElement([1]), 1)

    def test_majorityElement_twoElements(self):
        s = Solution()
        self.assertEqual(s.majorityElement([1, 2]), 0)

    def test_majorityElement_oddLength(self):
        s = Solution()
        self.assertEqual(s.majorityElement([1, 2, 1]), 1)

    def test_majorityElement_evenLength(self):
        s = Solution()
        self.assertEqual(s.majorityElement([1, 2, 2, 1]), 0)

    def test_majorityElement_multipleMajority(self):
        s = Solution()
        self.assertEqual(s.majorityElement([1, 2, 2, 1, 2]), 2)


if __name__ == "__main__":
    unittest.main()
