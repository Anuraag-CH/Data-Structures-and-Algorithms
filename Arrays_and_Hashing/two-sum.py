# https://leetcode.com/problems/two-sum

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hashmap = {}

        hashmap[nums[0]] = 0

        for i in range(1, len(nums)):
            if target - nums[i] in hashmap:
                return [hashmap[target - nums[i]], i]
            else:
                hashmap[nums[i]] = i


# Time Complexity: O(n)
# Space Complexity: O(n)
