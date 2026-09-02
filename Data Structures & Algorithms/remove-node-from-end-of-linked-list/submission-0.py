# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        node = head
        count = 0

        #Find length of linked list
        while node:
            count += 1
            node = node.next
        
        #Find pos of node to remove, edgecase
        pos = count - n
        if pos == 0:
            return head.next
        
        node = head
        for i in range(count):
            if i == pos - 1:
                node.next = node.next.next
                break
            node = node.next
        return head
