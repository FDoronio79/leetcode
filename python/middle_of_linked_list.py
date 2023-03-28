# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #create two pointers both starting starting at the head
        slow = fast = head

        #loop if fast is not null and fast.next is not null to make sure we're not hitting any excpetions
        #when fast reaches the end of the list return slow pointer as it will point to the middle of the list
        while fast and fast.next:
            #move slow pointer 1 node over
            slow = slow.next
            #move fast pointer 2 nodes over
            fast = fast.next.next
        #return slow pointer
        return slow