# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        top = ListNode()
        end = top


        while list1 and list2:
            if list1.val <= list2.val:
                end.next = list1
                end = list1
                list1 = end.next
            else:
                end.next = list2
                end = list2
                list2 = end.next
            
        if list1 is None:
            end.next = list2
        elif list2 is None:
            end.next = list1

        return top.next

