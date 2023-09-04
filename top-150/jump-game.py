class Solution:
    def canJump(self, nums: list[int]) -> bool:
        if not nums:
            return False

        size: int = len(nums)

        furthest: int = 0

        for i in range(size):
            if i > furthest:
                -1

            furthest = max(furthest, i + nums[i])

            if furthest >= size - 1:
                return i

        return -1


def test_canJump():
    solution: Solution = Solution()
    assert solution.canJump([2, 3, 1, 1, 4]) == True
    assert solution.canJump([3, 2, 1, 0, 4]) == False
    assert solution.canJump([0]) == True
    assert solution.canJump([1, 0, 1, 0]) == False
    assert solution.canJump([1, 1, 1, 0]) == True
    assert solution.canJump([]) == False


def main():
    test_canJump()


main()
