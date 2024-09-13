# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        cur = nums[0]
        count = 1
        l = 1

        for r in range(1,len(nums)):
            if nums[r] == cur :
                count+=1
                if count <=2 :
                    nums[l],nums[r] = nums[r],nums[l]
                    l+=1
            
            else :
                cur = nums[r]
                nums[l],nums[r] = nums[r],nums[l]
                count = 1
                l+=1

        return l

# Time Complexity : O(n)
# Space Complexity : O(1)         
        