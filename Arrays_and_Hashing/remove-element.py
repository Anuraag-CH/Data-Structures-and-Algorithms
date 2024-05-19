# https://leetcode.com/problems/remove-element

from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l = 0
        for r in range(0, len(nums)):
            if nums[r] != val:
                nums[l] = nums[r]
                l += 1
        return l


# Time complexity: O(n)
# Space complexity: O(1)
