# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        if list1 is None and list2 is None: return None
        if list1 is None: return list2
        if list2 is None: return list1
        
        truehead = list1 if list1.val <= list2.val else list2
        temp = None

        while list1 is not None and list2 is not None:
            if list1.val <= list2.val:
                temp = list1.next
                list1.next = list2
                list1 = temp
            else:
                temp = list2.next
                list2.next = list1
                list2 = temp

        return truehead