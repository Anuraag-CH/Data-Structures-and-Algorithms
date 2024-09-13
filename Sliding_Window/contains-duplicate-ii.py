# https://leetcode.com/problems/contains-duplicate-ii

from typing import List

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        l = 0
        hash_set = set()

        for r in range(len(nums)):
            
            if r-l > k :
                hash_set.remove(nums[l])
                l += 1
            
            
            if nums[r] in hash_set :
                return True
            hash_set.add(nums[r])
        
        return False

# Time complexity: O(n)
# Space complexity: O(k)
        