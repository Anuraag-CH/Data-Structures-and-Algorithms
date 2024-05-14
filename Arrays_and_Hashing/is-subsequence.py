# https://leetcode.com/problems/is-subsequence


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True
        i = 0
        for j in range(0, len(t)):
            if i == len(s):
                return True
            if s[i] == t[j]:
                i += 1

        return i == len(s)


# Time complexity: O(n)
# Space complexity: O(1)
