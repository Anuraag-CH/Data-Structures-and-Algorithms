# https://leetcode.com/problems/merge-two-sorted-lists/


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        res = ListNode()
        tail = res

        while list1 and list2 :
            if list1.val <= list2.val :
                tail.next = list1
                tail =tail.next
                list1 = list1.next
            
            else :
                tail.next = list2
                tail = tail.next
                list2 = list2.next
        

        if list1 == None :
            tail.next = list2
        
        if list2 == None :
            tail.next = list1
        
        return res.next

# Time Complexity : O(n)
            
        