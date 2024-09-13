# https://leetcode.com/problems/minimum-size-subarray-sum
from typing import List
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        total_sum = 0
        length = float('inf')
        left = 0

        for r in range(len(nums)):
            total_sum += nums[r]
            while total_sum >= target:
                length = min(length, r - left + 1)
                total_sum -= nums[left]
                left += 1
            
        return length if length != float('inf') else 0
    

# Time complexity: O(n)
# Space complexity: O(1)