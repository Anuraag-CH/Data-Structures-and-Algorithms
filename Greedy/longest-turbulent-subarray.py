# https://leetcode.com/problems/longest-turbulent-subarray

class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        if len(arr) == 1:
            return 1
        if len(arr) == 2:
            return 2 if arr[0] != arr[1] else 1
        
        max_len = 1
        curr_len = 1
        present_sign = ""

        for i in range(1, len(arr)):
            diff = arr[i] - arr[i-1]

            if diff == 0:
                curr_len = 1
                present_sign = ""
            
            elif diff > 0:
                curr_len = curr_len + 1 if present_sign == "<" else 2
                present_sign = ">"
            
            else:
                curr_len = curr_len + 1 if present_sign == ">" else 2
                present_sign = "<"
            
            max_len = max(max_len, curr_len)
        
        return max_len

# Time complexity: O(n)
# Space complexity: O(1)
        