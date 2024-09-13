# https://leetcode.com/problems/maximum-sum-circular-subarray

from typing import List

class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:

        max_sum = float('-inf')
        min_sum = float('inf')
        cur_sum_max = 0
        cur_sum_min = 0
        total_sum = 0

        for n in nums:
            total_sum += n
            cur_sum_max = max(0, cur_sum_max)+n
            cur_sum_min = min(0, cur_sum_min)+n
            max_sum = max(max_sum, cur_sum_max)
            min_sum = min(min_sum, cur_sum_min)
        
        return max(max_sum, total_sum-min_sum) if max_sum > 0 else max_sum


# Time complexity: O(n)
# Space complexity: O(1)