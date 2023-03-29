class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode()
        tail = result
        
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2
        return result.next
    
#if you want to walk through the code locally
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:        
    def mergeLists(self, list1, list2) -> ListNode:
        result = ListNode()
        tail = result
        
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2
        return result.next
    
def createdLinkedList(lst):
    head = None
    for val in reversed(lst):
        head = ListNode(val, head)
    return head

def toList(head):
    lst = []
    while head:
        lst.append(head.val)
        head = head.next
    return lst

list1 = createdLinkedList([1,2,4])
list2 = createdLinkedList([1,3,4])

test = Solution()
print(toList(test.mergeLists(list1, list2)))
        
