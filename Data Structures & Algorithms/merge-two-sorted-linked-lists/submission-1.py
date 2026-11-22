# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        curr, n1, n2 = None, list1, list2

        if list1 is None and list2 is None:
            return None
        elif list1 is None:
            return list2
        elif list2 is None:
            return list1

        if list1.val <= list2.val:
            curr = list1
            n1 = curr.next
        else:
            curr = list2
            n2 = curr.next
        
        truehead = curr

        while n1 is not None and n2 is not None:
            if n1.val <= n2.val:
                curr.next = n1
                curr = n1
                n1 = curr.next
            else:
                curr.next = n2
                curr = n2
                n2 = curr.next
            
        if n1 is None and n2 is not None:
            curr.next = n2
        elif n2 is None and n1 is not None:
            curr.next = n1

        return truehead

