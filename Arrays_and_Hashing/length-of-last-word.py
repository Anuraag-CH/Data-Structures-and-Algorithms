# https://leetcode.com/problems/length-of-last-word
from typing import List


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        length = 0
        i = len(s) - 1

        while s[i] == " ":
            i -= 1

        for i in range(i, -1, -1):
            if s[i] == " ":
                return length
            length += 1

        return length


# Time complexity: O(n)
# Space complexity: O(1)
