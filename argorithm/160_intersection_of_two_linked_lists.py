# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        na, nb = headA, headB
        
        while na!=nb:
            if na is None:
                na = headB
            else:
                na = na.next
            if nb is None:
                nb = headA
            else:
                nb = nb.next
        return na