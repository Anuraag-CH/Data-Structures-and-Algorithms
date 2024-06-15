# https://leetcode.com/problems/product-of-array-except-self

from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        count_zero = 0
        product = 1

        for n in nums:
            if n == 0:
                count_zero += 1
            else:
                product *= n

        if count_zero > 1:
            return [0] * len(nums)

        if count_zero == 1:
            return [0 if n != 0 else product for n in nums]

        return [product // n for n in nums]


# Time complexity: O(n)
# Space complexity: O(1)

# Another approach


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        res = [1] * len(nums)

        for i in range(1, len(nums)):
            res[i] = res[i - 1] * nums[i - 1]

        right = 1

        for i in range(len(nums) - 1, -1, -1):
            res[i] *= right
            right *= nums[i]

        return res


# Time complexity: O(n)
# Space complexity: O(1)
