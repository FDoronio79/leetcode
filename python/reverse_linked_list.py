# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # create two pointers to keep track of the current node and previous node
        # previous node will always be behind current node so start previous at None
        prev = None
        # start current at head because we start at the beginning of the list
        current = head

        #while current is not equal to null continue to iterate
        while current:
            #create a variable to keep track of the next value after current so we can updated current to this value
            next = current.next
            #take the next pointer of current and reverse it to set to previous before breaking the link
            current.next = prev
            #shift the previous pointer to the current pointer current pointer because we'll shift the current pointer to the value of next
            prev = current
            #shift the current pointer to the value of next
            current = next
        #return previous pointer because previous should no equal the new head
        return prev
        