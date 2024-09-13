# https://leetcode.com/problems/container-with-most-water

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        l= 0
        r =len(heights)-1
        
        while l<r :
            max_area = max(max_area,(r-l)*min(heights[l],heights[r]))

            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
        
        return max_area

# Time complexity: O(n)
# Space complexity: O(1)




        





        