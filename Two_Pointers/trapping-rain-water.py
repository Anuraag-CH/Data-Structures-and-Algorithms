# https://leetcode.com/problems/trapping-rain-water
from typing import List
class Solution:
    def trap(self, height: List[int]) -> int:

        #get max height from left

        left_max = [-1]
        cur = height[0]
        for i in range(1,len(height)):
            cur = max(cur,height[i])
            left_max.append(cur)
        
        #get max height from right

        right_max = [-1]
        cur = height[-1]
        for i in range(len(height)-2,-1,-1):
            
            cur = max(cur,height[i])
            right_max.insert(0,cur)
        

        #calculate water trapped

        water = 0
        for i in range(len(height)):
            
            min_value = min(left_max[i],right_max[i]) 
            water_trapped = min_value - height[i]
            if water_trapped > 0:
                water += water_trapped
        return water

# Time complexity: O(n)
# Space complexity: O(n)


#Another approach using two pointers

class Solution:
    def trap(self, height: List[int]) -> int:

        l = 0
        r = len(height)-1
        
        left_max = height[l]
        right_max = height[r]
        res = 0

        while l<r:

            if left_max < right_max:
                l += 1
                left_max = max(left_max,height[l])
                res += left_max - height[l]
            else:
                r -= 1
                right_max = max(right_max,height[r])
                res += right_max - height[r]
        
        return res

# Time complexity: O(n)
# Space complexity: O(1)
