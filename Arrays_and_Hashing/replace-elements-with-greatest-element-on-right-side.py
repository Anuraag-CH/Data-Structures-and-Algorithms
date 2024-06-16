# https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side

from typing import List


class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        res = [-1]

        if len(arr) == 1:
            return res

        greatest_element = arr[-1]

        for i in range(len(arr) - 1, 0, -1):
            greatest_element = max(greatest_element, arr[i])
            res.append(greatest_element)

        return reversed(res)


# Time complexity: O(n)
# Space complexity: O(n)
