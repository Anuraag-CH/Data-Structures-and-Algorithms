# https://leetcode.com/problems/valid-anagram


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        dict_s = {}
        dict_t = {}

        for i in s:
            dict_s[i] = dict_s.get(i, 0) + 1

        for i in t:
            dict_t[i] = dict_t.get(i, 0) + 1

        return dict_s == dict_t


# Time Complexity: O(n)
# Space Complexity: O(n)
