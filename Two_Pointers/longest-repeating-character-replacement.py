# https://leetcode.com/problems/longest-repeating-character-replacement


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        hashmap = {}
        l = 0   
        r = 0
        max_len = 0
        

        while r < len(s):
            hashmap[s[r]] = hashmap.get(s[r], 0) + 1
            
            if r - l + 1 - max(hashmap.values()) <= k:
                max_len = max(max_len, r - l + 1)
            
            else:
                hashmap[s[l]] -= 1
                l += 1
            
            r += 1
        
        return max_len


# Time complexity: O(n)
# Space complexity: O(1)
            
            


