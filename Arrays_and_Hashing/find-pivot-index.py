# https://leetcode.com/problems/find-pivot-index

from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:

        total = sum(nums)
        left_sum = 0
        for i in range(len(nums)):
            left_sum += nums[i]
            right_sum = total - left_sum
            if left_sum - nums[i] == right_sum:
                return i

        return -1


# Time complexity: O(n)
# Space complexity: O(n)
