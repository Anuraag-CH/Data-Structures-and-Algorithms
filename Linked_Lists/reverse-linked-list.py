# https://leetcode.com/problems/reverse-linked-list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        prev = None
        cur = head

        while cur :
            cur = cur.next
            head.next = prev
            prev = head 
            head= cur
        
        return prev


# Time Complexity : O(n)
# Space Complexity : O(1)



        