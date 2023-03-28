# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        #start with two pointers both pointing at the head
        prev = curr = head

        #while curr and curr.next are not null continue looping, check curr.next in case it is null then that means curr.next.next is also null
        while curr and curr.next:
            #move prev pointer up 1
            prev = prev.next
            #move curr pointer up 2
            curr = curr.next.next
            #if curr pointer catches up to prev pointer then that means there is a loop
            if prev == curr:
                return True 
        #otherwise return False
        return False