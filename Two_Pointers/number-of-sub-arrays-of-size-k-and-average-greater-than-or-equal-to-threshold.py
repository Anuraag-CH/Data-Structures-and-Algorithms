# https://leetcode.com/problems/number-of-sub-arrays-of-size-k-and-average-greater-than-or-equal-to-threshold

from typing import List

class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        l = 0
        current_sum = sum(arr[0:k])
        count = 0

        if current_sum / k >= threshold :
            count+=1 


        for r in range(k,len(arr)):
            
            current_sum = current_sum-arr[l]+arr[r]
            l+=1
            if current_sum / k >= threshold :
                count+=1
        
        return count

# Time complexity: O(n)
# Space complexity: O(1)

