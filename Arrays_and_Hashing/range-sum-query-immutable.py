# https://leetcode.com/problems/range-sum-query-immutable

from typing import List


class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix_sum = []
        total = 0
        for i in nums:
            total += i
            self.prefix_sum.append(total)

    def sumRange(self, left: int, right: int) -> int:

        if left == 0:
            return self.prefix_sum[right]
        else:
            return self.prefix_sum[right] - self.prefix_sum[left - 1]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)

# Time complexity: O(n) for __init__ and O(1) for sumRange
# Space complexity: O(n) for __init__ and O(1) for sumRange
