#https://leetcode.com/problems/merge-two-sorted-lists/submissions/1968805708/?envType=study-plan-v2&envId=top-interview-150

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        ptr1 = list1
        ptr2 = list2
        if ptr1 is None and ptr2 is None:
            return None
        elif ptr1 is None and ptr2 is not None:
            return ptr2
        elif ptr1 is not None and ptr2 is None:
            return ptr1
        # We always want to start our head at the smaller value
        if ptr1.val > ptr2.val:
            ptr1, ptr2 = ptr2, ptr1
        head = ptr1
        while ptr1.next is not None and ptr2 is not None:
            if ptr1.val <= ptr2.val and ptr1.next.val >= ptr2.val:
                temp = ptr2
                ptr2 = temp.next
                temp.next = ptr1.next
                ptr1.next = temp
                ptr1 = ptr1.next
            else: 
                ptr1 = ptr1.next
        if ptr2 is not None:
            ptr1.next = ptr2
        return head
