class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        def reverse(nums, start, end):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start, end = start + 1, end - 1

        n = len(nums)
        if n == 0:
            return
        k = k % n

        reverse(nums, 0, n - 1)
        reverse(nums, 0, k - 1)
        reverse(nums, k, n - 1)


def test_rotate():
    s = Solution()

    # Test case 1: Rotate by 0
    nums = [1, 2, 3, 4, 5, 6, 7]
    k = 0
    s.rotate(nums, k)
    assert nums == [1, 2, 3, 4, 5, 6, 7]

    # Test case 2: Rotate by 1
    nums = [1, 2, 3, 4, 5, 6, 7]
    k = 1
    s.rotate(nums, k)
    assert nums == [7, 1, 2, 3, 4, 5, 6]

    # Test case 3: Rotate by n
    nums = [1, 2, 3, 4, 5, 6, 7]
    k = len(nums)
    s.rotate(nums, k)
    assert nums == [1, 2, 3, 4, 5, 6, 7]

    # Test case 4: Rotate by k > n
    nums = [1, 2, 3, 4, 5, 6, 7]
    k = 10
    s.rotate(nums, k)
    assert nums == [5, 6, 7, 1, 2, 3, 4]

    # Test case 5: Rotate by k = n/2
    nums = [1, 2, 3, 4, 5, 6, 7]
    k = len(nums) // 2
    s.rotate(nums, k)
    assert nums == [5, 6, 7, 1, 2, 3, 4]

    # Test case 6: Rotate an empty list
    nums = []
    k = 3
    s.rotate(nums, k)
    assert nums == []

    # Test case 7: Rotate a list with one element
    nums = [1]
    k = 1
    s.rotate(nums, k)
    assert nums == [1]


test_rotate()
