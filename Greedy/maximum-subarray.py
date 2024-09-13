# https://leetcode.com/problems/maximum-subarray

from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        max_sum = float('-inf')
        current_sum = 0

        for n in nums:
            current_sum = max(0,current_sum)
            current_sum += n
            max_sum = max(max_sum, current_sum)
        
        return max_sum

# Time complexity: O(n)
# Space complexity: O(1)
        