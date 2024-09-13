# https://leetcode.com/problems/longest-substring-without-repeating-characters

from typing import List

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        length = float("-inf")
        hashset = set()

        for r in range(len(s)):
            while s[r] in hashset :
                hashset.remove(s[l])
                l+=1
            hashset.add(s[r])
            length = max(length, r-l+1)
        return length if length != float("-inf") else 0


# Time complexity: O(n)
# Space complexity: O(1)





