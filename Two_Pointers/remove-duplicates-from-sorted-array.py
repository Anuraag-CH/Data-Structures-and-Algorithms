# https://leetcode.com/problems/remove-duplicates-from-sorted-array

from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        i = 0

        for j in range(0,len(nums)):
            if nums[j] != nums[i] :
                i+=1
                nums[i],nums[j] = nums[j],nums[i]
            j+=1
            
        return i+1

# Time complexity: O(n)
# Space complexity: O(1)
        