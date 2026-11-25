# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        # fast slow method to find middle
        # START FAST 1 AHEAD so that slow lands one BEFORE the end of the list
        # so that you can have the first half tail point to null first,
        # then reverse second half of list
        slow, fast = head, head.next
        while fast:
            slow = slow.next
            fast = fast.next
            if fast:
                fast = fast.next

        # end first list
        second = slow.next # 6
        slow.next = None # make 4 point to None

        # reverse second half
        prev = None
        while second:
            next = second.next
            second.next = prev
            prev = second
            second = next
        # prev is head of flipped list

        # merge lists
        front = head
        while prev:
            t1, t2 = front.next, prev.next
            front.next = prev
            prev.next = t1
            front, prev = t1, t2

