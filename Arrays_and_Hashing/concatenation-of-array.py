# https://leetcode.com/problems/concatenation-of-array

from typing import List


class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:

        n = 2
        ans = []

        while n > 0:
            for i in range(0, len(nums)):
                ans.append(nums[i])
            n -= 1

        return ans


# Time complexity: O(n)
# Space complexity: O(n)
