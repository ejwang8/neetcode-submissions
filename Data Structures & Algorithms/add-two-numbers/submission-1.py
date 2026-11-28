# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        # do we need a dummy node? since guaranteed NON EMPTY
        # i guess so if we do in place bc we need to set NEXT node as val

        dummy = ListNode(0)
        dummy.next = l1
        curr = dummy
        carryVal = 0

        while l1 and l2 or carryVal:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            val = v1 + v2 + carryVal # 5

            if curr.next:
                print(curr.val)
                curr.next.val = val % 10 # try in place
            else:
                print("does this run")
                curr.next = ListNode(val % 10)
            carryVal = val // 10
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            curr = curr.next
        
        return dummy.next
